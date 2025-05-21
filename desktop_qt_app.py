import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QListWidgetItem,
    QRadioButton, QButtonGroup, QDialog, QLineEdit,
    QDialogButtonBox, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMenu, QSpacerItem, QSizePolicy # Added QSpacerItem, QSizePolicy
from data_manager import Todo, init_db

class TaskDialog(QDialog):
    """
    A dialog window for adding or editing a task.
    It contains a QLineEdit for the task title and OK/Cancel buttons.
    """
    def __init__(self, parent=None, current_title="", window_title="Task"):
        """
        Constructs the TaskDialog.
        
        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
            current_title (str, optional): The current title for editing. Defaults to "".
            window_title (str, optional): The title of the dialog window. Defaults to "Task".
        """
        super().__init__(parent)
        self.setWindowTitle(window_title)
        self.setObjectName("TaskDialog") # For specific styling if needed
        self.layout = QVBoxLayout(self)

        self.title_edit = QLineEdit(current_title)
        self.title_edit.setPlaceholderText("Enter task title...")
        self.layout.addWidget(self.title_edit)
        self.title_edit.setFocus() # Automatically focus the input field

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept) # Connect OK to accept()
        self.button_box.rejected.connect(self.reject) # Connect Cancel to reject()
        self.layout.addWidget(self.button_box)

    def get_title(self):
        """
        Retrieves the stripped text from the title QLineEdit.
        
        Returns:
            str: The task title entered by the user.
        """
        return self.title_edit.text().strip()

class MainWindow(QMainWindow):
    """
    The main application window for the To-Do List.
    It displays the list of tasks, action buttons (Add, Edit, Delete),
    filter radio buttons (All, Active, Completed), and integrates with
    the system tray.
    """
    def __init__(self):
        """Initializes the MainWindow, sets up UI elements, and loads initial tasks."""
        super().__init__()
        self.setWindowTitle("My To-Do List")
        self.setGeometry(100, 100, 800, 600) # x, y, width, height

        init_db() # Ensure the database is initialized

        self.current_filter = "all" # Default filter when the app starts

        # Setup main layout and central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.task_list_widget = QListWidget()
        self.task_list_widget.itemSelectionChanged.connect(self.update_button_states)
        self.task_list_widget.itemDoubleClicked.connect(self.toggle_task_completion)
        self.layout.addWidget(self.task_list_widget)

        # --- Action Buttons ---
        self.action_buttons_layout = QHBoxLayout()
        self.add_task_button = QPushButton("Add Task")
        self.add_task_button.clicked.connect(self.open_add_task_dialog)
        self.edit_task_button = QPushButton("Edit Task")
        self.edit_task_button.clicked.connect(self.open_edit_task_dialog)
        self.delete_task_button = QPushButton("Delete Task")
        self.delete_task_button.clicked.connect(self.delete_selected_task)
        
        self.edit_task_button.setEnabled(False) # Initially disabled
        self.delete_task_button.setEnabled(False) # Initially disabled

        # Spacer to push buttons to the right, adjust as needed for preferred alignment
        self.action_buttons_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.action_buttons_layout.addWidget(self.add_task_button)
        self.action_buttons_layout.addWidget(self.edit_task_button)
        self.action_buttons_layout.addWidget(self.delete_task_button)
        self.layout.addLayout(self.action_buttons_layout)

        # --- Filter Radio Buttons ---
        self.filter_buttons_layout = QHBoxLayout()
        self.filter_group = QButtonGroup(self) # Manages exclusivity of radio buttons
        
        self.all_radio = QRadioButton("All")
        self.all_radio.setChecked(True) # Default filter
        self.all_radio.toggled.connect(lambda: self.apply_filter("all"))
        
        self.active_radio = QRadioButton("Active")
        self.active_radio.toggled.connect(lambda: self.apply_filter("active"))
        
        self.completed_radio = QRadioButton("Completed")
        self.completed_radio.toggled.connect(lambda: self.apply_filter("completed"))
        
        # Add radio buttons to the button group and layout
        self.filter_group.addButton(self.all_radio)
        self.filter_group.addButton(self.active_radio)
        self.filter_group.addButton(self.completed_radio)
        self.filter_buttons_layout.addWidget(self.all_radio)
        self.filter_buttons_layout.addWidget(self.active_radio)
        self.filter_buttons_layout.addWidget(self.completed_radio)
        self.layout.addLayout(self.filter_buttons_layout)

        # --- System Tray Icon and Initial Load ---
        self.init_tray_icon()
        self.load_tasks() # Load tasks based on the default filter

    def init_tray_icon(self):
        """Initializes the system tray icon and its context menu."""
        # tray_icon.png (32x32) should be in the same directory as the script.
        # If not found, Qt may show a default icon or no icon.
        self.tray_icon = QSystemTrayIcon(QIcon("tray_icon.png"), self)
        self.tray_icon.setToolTip("To-Do List Desktop App - My To-Do List") # More descriptive tooltip
        
        tray_menu = QMenu()
        show_action = QAction("Show App", self)
        show_action.triggered.connect(self.show_app_from_tray)
        tray_menu.addAction(show_action)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(QApplication.instance().quit) # Quit the application
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def show_app_from_tray(self):
        """Shows the main window when 'Show App' is clicked in the tray menu."""
        self.showNormal() # Restores the window if minimized or hidden
        self.activateWindow() # Brings the window to the foreground

    def apply_filter(self, filter_type):
        """
        Applies the selected filter to the task list.
        Called when a radio button is toggled.

        Args:
            filter_type (str): The type of filter to apply ("all", "active", "completed").
        """
        # Ensure the signal is processed only when a radio button is checked (not when unchecked during a group switch)
        if self.sender() and self.sender().isChecked():
            self.current_filter = filter_type
            self.load_tasks()

    def load_tasks(self):
        """
        Loads tasks from the database based on the current filter
        and populates the task_list_widget.
        """
        self.task_list_widget.clear() # Clear existing items before loading new ones
        
        # Fetch tasks based on the current filter
        if self.current_filter == "all":
            tasks = Todo.get_all()
        elif self.current_filter == "active":
            tasks = Todo.get_active()
        elif self.current_filter == "completed":
            tasks = Todo.get_completed()
        else:
            tasks = [] # Should ideally not happen with radio buttons

        # Populate the list widget
        for task in tasks:
            item = QListWidgetItem(task.title)
            item.setData(Qt.UserRole, task.id) # Store task ID for later retrieval
            item.setData(Qt.UserRole + 1, task.complete) # Store completion status
            
            # Apply strikethrough style for completed tasks
            font = item.font()
            font.setStrikeOut(task.complete)
            item.setFont(font)
            
            self.task_list_widget.addItem(item)
        
        self.update_button_states() # Update button states after loading/reloading tasks

    def update_button_states(self):
        """
        Enables or disables the 'Edit Task' and 'Delete Task' buttons
        based on whether an item is selected in the task list.
        """
        is_task_selected = bool(self.task_list_widget.selectedItems())
        self.edit_task_button.setEnabled(is_task_selected)
        self.delete_task_button.setEnabled(is_task_selected)

    def open_add_task_dialog(self):
        """Opens the TaskDialog for adding a new task."""
        dialog = TaskDialog(self, window_title="Add New Task")
        if dialog.exec(): # QDialog.exec() returns True if accepted (OK), False if rejected (Cancel)
            title = dialog.get_title()
            if title:
                Todo.add(title)
                self.load_tasks() # Refresh the list
                # Show notification if tray icon is available and visible
                if hasattr(self, 'tray_icon') and self.tray_icon.isVisible():
                    self.tray_icon.showMessage("Task Added", f"The new task '{title}' has been added.")
            else:
                QMessageBox.warning(self, "Warning", "Task title cannot be empty.")

    def open_edit_task_dialog(self):
        """Opens the TaskDialog for editing the selected task."""
        selected_items = self.task_list_widget.selectedItems()
        if not selected_items:
            return # Should not happen if edit_task_button is properly disabled
        
        item = selected_items[0]
        task_id = item.data(Qt.UserRole)
        current_title = item.text() # Get current title from the list item

        dialog = TaskDialog(self, current_title=current_title, window_title="Edit Task")
        if dialog.exec():
            new_title = dialog.get_title()
            if new_title and new_title != current_title:
                Todo.update_title(task_id, new_title)
                self.load_tasks() # Refresh the list
            elif not new_title: # Title was cleared or only whitespace
                QMessageBox.warning(self, "Warning", "Task title cannot be empty.")
            # If new_title is the same as current_title, do nothing.

    def delete_selected_task(self):
        """Deletes the selected task after confirmation."""
        selected_items = self.task_list_widget.selectedItems()
        if not selected_items:
            return # Should not happen if delete_task_button is properly disabled

        item = selected_items[0]
        task_id = item.data(Qt.UserRole)
        task_title = item.text() # For the confirmation message
        
        # Confirmation dialog
        reply = QMessageBox.question(self, "Confirm Delete", 
                                     f"Are you sure you want to delete '{task_title}'?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No) # Default to No
        
        if reply == QMessageBox.Yes:
            Todo.delete(task_id)
            self.load_tasks() # Refresh the list

    def toggle_task_completion(self, item):
        """
        Toggles the completion status of the double-clicked task.
        
        Args:
            item (QListWidgetItem): The list item that was double-clicked.
        """
        if not item: # Should not be necessary with itemDoubleClicked signal but good practice
            return
            
        task_id = item.data(Qt.UserRole)
        task_title = item.text() 
        current_status = item.data(Qt.UserRole + 1) # Fetch stored completion status
        new_status = not current_status
        
        Todo.update_complete(task_id, new_status)
        
        if new_status: # If task is now marked as complete
            # Show notification if tray icon is available and visible
            if hasattr(self, 'tray_icon') and self.tray_icon.isVisible():
                self.tray_icon.showMessage("Task Completed", f"The task '{task_title}' has been marked as complete.")
        
        self.load_tasks() # Refresh the list to update style and potentially filter


if __name__ == "__main__":
    app = QApplication(sys.argv) # Must be created before any QWidgets

    # --- Global Stylesheet ---
    stylesheet = """
        QWidget {
            font-size: 10pt; /* Default font size */
        }
        QMainWindow {
            background-color: #f0f0f0; /* Light gray background for main window */
        }
        QPushButton {
            padding: 6px 10px; /* Adjusted padding */
            background-color: #007bff; /* Bootstrap primary blue */
            color: white;
            border: 1px solid #007bff; /* Border to match background */
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #0056b3; /* Darker blue on hover */
            border-color: #0056b3;
        }
        QPushButton:pressed {
            background-color: #004085; /* Even darker blue when pressed */
            border-color: #004085;
        }
        QPushButton:disabled {
            background-color: #c0c0c0; /* Gray when disabled */
            color: #808080;
            border-color: #c0c0c0;
        }
        QListWidget {
            border: 1px solid #ccc;
            border-radius: 4px;
            background-color: white;
        }
        QListWidget::item {
            padding: 5px; /* Padding for list items */
            border-bottom: 1px dotted #eee; /* Separator for items */
        }
        QListWidget::item:selected {
            background-color: #007bff; /* Blue selection */
            color: white;
        }
        QLineEdit {
            padding: 4px; /* Padding for line edits */
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        QRadioButton {
            spacing: 5px; /* Space between radio button and text */
        }
        QDialog#TaskDialog { /* Target TaskDialog specifically by object name */
             background-color: #f8f9fa; /* Lighter gray for dialogs */
        }
        /* Example of styling a specific label if it had an object name */
        /* QLabel#ErrorLabel { 
            color: red;
            font-weight: bold;
        } */
        QMessageBox {
            font-size: 10pt; /* Ensure message box uses app font size */
        }
    """
    app.setStyleSheet(stylesheet)
    
    # --- Tray Icon Availability and Application Exit Logic ---
    tray_icon_available = QSystemTrayIcon.isSystemTrayAvailable()
    if tray_icon_available:
        # If system tray is available, the app should not quit when the last window is closed.
        # It should remain running in the tray.
        QApplication.setQuitOnLastWindowClosed(False)
    else:
        # If no system tray, the app should quit when the main window is closed.
        print("System tray not available. Notifications might not work as expected. "
              "App will close when the main window is closed.")
        QApplication.setQuitOnLastWindowClosed(True)
    
    # --- Initialize and Show Main Window ---
    window = MainWindow()
    window.show() # Display the main window
    
    sys.exit(app.exec()) # Start the Qt event loop
