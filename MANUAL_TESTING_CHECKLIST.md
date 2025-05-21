# Manual Testing Checklist for To-Do List Desktop App (`desktop_qt_app.py`)

This checklist provides steps for manually testing the functionality and appearance of the Qt-based To-Do List desktop application.

**Testing Environment Setup:**
*   Ensure Python is installed.
*   Ensure PySide6 and Pillow are installed (`pip install PySide6 Pillow`).
*   Ensure `data_manager.py` is in the same directory as `desktop_qt_app.py`.
*   Ensure `tray_icon.png` (a 32x32 checkmark icon, if generated) is present in the same directory.
*   Run the application using `python desktop_qt_app.py`.
*   For tests involving the system tray, ensure you are running in a desktop environment where system tray icons are supported.

---

## I. Core CRUD Operations

### 1. Adding a New Task
*   [ ] Click the "Add Task" button.
*   [ ] **Verify**: The "Add New Task" dialog appears.
*   [ ] **Verify**: The input field in the dialog has focus automatically.
*   [ ] **Verify**: The input field shows "Enter task title..." as placeholder text.
*   [ ] Enter a valid task title (e.g., "Test Task 1").
*   [ ] Click "OK".
*   [ ] **Verify**: The new task appears in the main list.
*   [ ] **Verify**: The task is not struck through (i.e., it's active).

### 2. Attempting to Add a Task with an Empty Title
*   [ ] Click the "Add Task" button.
*   [ ] Leave the title field empty.
*   [ ] Click "OK".
*   [ ] **Verify**: A warning message box appears with the text "Task title cannot be empty."
*   [ ] **Verify**: No new task is added to the list.
*   [ ] Close the warning message and the "Add New Task" dialog.

### 3. Editing an Existing Task
*   [ ] Add a task if none exists (e.g., "Task to Edit").
*   [ ] Select the task "Task to Edit" in the list.
*   [ ] Click the "Edit Task" button.
*   [ ] **Verify**: The "Edit Task" dialog appears.
*   [ ] **Verify**: The input field is pre-filled with "Task to Edit".
*   [ ] **Verify**: The input field in the dialog has focus automatically.
*   [ ] Change the title (e.g., to "Edited Task Title").
*   [ ] Click "OK".
*   [ ] **Verify**: The task in the list is updated to "Edited Task Title".

### 4. Attempting to Edit a Task to Have an Empty Title
*   [ ] Add a task if none exists (e.g., "Task for Empty Edit").
*   [ ] Select the task "Task for Empty Edit".
*   [ ] Click the "Edit Task" button.
*   [ ] Clear the title field completely.
*   [ ] Click "OK".
*   [ ] **Verify**: A warning message box appears with the text "Task title cannot be empty."
*   [ ] **Verify**: The task title in the list remains "Task for Empty Edit".
*   [ ] Close the warning message and the "Edit Task" dialog.

### 5. Marking a Task as Complete
*   [ ] Add a new, active task if none exists (e.g., "Complete This Task").
*   [ ] Double-click on the "Complete This Task" item in the list.
*   [ ] **Verify**: The task "Complete This Task" now has a strikethrough style.
*   [ ] **Verify**: If the "Active" filter is on, the task disappears from the list. If "All" or "Completed" is on, it remains/appears and is struck through.

### 6. Marking a Completed Task as Incomplete
*   [ ] Ensure there is a completed task (e.g., "Complete This Task" from the previous step).
*   [ ] Double-click on the completed task "Complete This Task".
*   [ ] **Verify**: The strikethrough style is removed from "Complete This Task".
*   [ ] **Verify**: If the "Completed" filter is on, the task disappears. If "All" or "Active" is on, it remains/appears and is not struck through.

### 7. Deleting a Task
*   [ ] Add a task if none exists (e.g., "Task to Delete").
*   [ ] Select "Task to Delete" in the list.
*   [ ] Click the "Delete Task" button.
*   [ ] **Verify**: A confirmation dialog appears, asking "Are you sure you want to delete 'Task to Delete'?".
*   [ ] Click "Yes".
*   [ ] **Verify**: The task "Task to Delete" is removed from the list.
*   [ ] Add another task (e.g., "Task Not to Delete").
*   [ ] Select "Task Not to Delete".
*   [ ] Click "Delete Task".
*   [ ] Click "No" on the confirmation dialog.
*   [ ] **Verify**: "Task Not to Delete" remains in the list.

---

## II. Filtering

### 1. Switching Filters
*   [ ] Add several tasks. Mark some as complete, leave others active. (e.g., "Active Task 1", "Completed Task 1", "Active Task 2").
*   [ ] **Initial State**: "All" filter should be selected by default.
*   [ ] **Verify**: All tasks ("Active Task 1", "Completed Task 1", "Active Task 2") are visible. "Completed Task 1" is struck through.
*   [ ] Select the "Active" radio button.
*   [ ] **Verify**: Only "Active Task 1" and "Active Task 2" are visible. Neither is struck through.
*   [ ] Select the "Completed" radio button.
*   [ ] **Verify**: Only "Completed Task 1" is visible and is struck through.
*   [ ] Select the "All" radio button again.
*   [ ] **Verify**: All tasks are visible, with completed ones struck through.

### 2. Filters After Task Modifications
*   [ ] With the "Active" filter selected:
    *   [ ] Add a new task "Active Task 3". **Verify**: It appears in the list.
    *   [ ] Double-click "Active Task 3" to complete it. **Verify**: It disappears from the "Active" list.
*   [ ] Switch to the "Completed" filter.
    *   [ ] **Verify**: "Active Task 3" (now completed) appears in this list.
    *   [ ] Double-click "Active Task 3" to mark it active again. **Verify**: It disappears from the "Completed" list.
*   [ ] Switch to the "Active" filter.
    *   [ ] **Verify**: "Active Task 3" (now active again) appears in this list.
    *   [ ] Select "Active Task 3" and delete it. **Verify**: It is removed from the list.
*   [ ] Edit an existing active task's title while on the "Active" filter. **Verify**: The title updates correctly in the list.
*   [ ] Edit an existing completed task's title while on the "Completed" filter. **Verify**: The title updates correctly in the list.

---

## III. Button States

*   [ ] **Initial State**:
    *   [ ] **Verify**: "Edit Task" button is disabled.
    *   [ ] **Verify**: "Delete Task" button is disabled.
*   [ ] Add a new task.
*   [ ] Select the newly added task in the list.
*   [ ] **Verify**: "Edit Task" button becomes enabled.
*   [ ] **Verify**: "Delete Task" button becomes enabled.
*   [ ] Click anywhere in the empty space of the list widget to deselect the task (if possible, or add a second task and select it, then select the first again to ensure selection change triggers state). *Alternatively, if direct deselection is hard, proceed to delete the task.*
    *   *(If direct deselection is possible)* **Verify**: "Edit Task" and "Delete Task" buttons become disabled again.
*   [ ] Select a task again.
*   [ ] Click "Delete Task" and confirm.
*   [ ] **Verify**: After the task is deleted and no other task is selected, "Edit Task" and "Delete Task" buttons are disabled.
*   [ ] Add multiple tasks. Select one, then select another. **Verify**: Buttons remain enabled.

---

## IV. Notifications (If System Tray is Available)

*Test these in an environment that supports system tray notifications.*

*   [ ] Add a new task "Notification Test Task".
*   [ ] **Verify**: A system tray notification appears with title "Task Added" and message "The new task 'Notification Test Task' has been added." (or similar).
*   [ ] Double-click "Notification Test Task" to mark it as complete.
*   [ ] **Verify**: A system tray notification appears with title "Task Completed" and message "The task 'Notification Test Task' has been marked as complete." (or similar).
*   [ ] Double-click "Notification Test Task" again to mark it as active.
*   [ ] **Verify**: No notification is shown for marking a task as active.

---

## V. System Tray Icon (If System Tray is Available)

*Test these in an environment that supports system tray icons.*

*   [ ] **Visibility**:
    *   [ ] **Verify**: A tray icon is visible in the system tray.
    *   [ ] **Verify**: The icon is `tray_icon.png` (checkmark on dark gray, if generated correctly). If not, note the appearance.
*   [ ] **Tooltip**:
    *   [ ] Hover the mouse cursor over the tray icon.
    *   [ ] **Verify**: The tooltip "To-Do List Desktop App" appears.
*   [ ] **Context Menu - "Show App"**:
    *   [ ] Minimize or hide the main application window (if possible through window manager, or by closing it if `QApplication.setQuitOnLastWindowClosed(False)` is active).
    *   [ ] Right-click on the system tray icon.
    *   [ ] Click "Show App".
    *   [ ] **Verify**: The main application window becomes visible and active.
*   [ ] **Context Menu - "Quit"**:
    *   [ ] Right-click on the system tray icon.
    *   [ ] Click "Quit".
    *   [ ] **Verify**: The application closes completely.

---

## VI. Window Behavior

### 1. Main Window Title
*   [ ] **Verify**: The main application window's title bar displays "My To-Do List".

### 2. Closing the Main Window (Simulate 'X' button)
*   **Scenario 1: System Tray is NOT Available**
    *   (Tester might need to simulate this by temporarily disabling tray or running in a minimal environment if possible; otherwise, rely on code review for `QApplication.setQuitOnLastWindowClosed(True)` behavior).
    *   [ ] Close the main window.
    *   [ ] **Verify**: The application quits entirely.
*   **Scenario 2: System Tray IS Available**
    *   [ ] Close the main window (click the 'X' button or equivalent).
    *   [ ] **Verify**: The main application window hides (or minimizes).
    *   [ ] **Verify**: The application continues running (system tray icon is still present).
    *   [ ] Use the "Show App" or "Quit" action from the tray icon context menu to interact further.

---

## VII. Styling and General Appearance

*   [ ] **Overall Look and Feel**:
    *   [ ] Observe the general font. Is it consistently applied and readable (expected: 10pt)?
    *   [ ] Check `QPushButton` style: padding (6px 10px), background color (#007bff), text color (white), border-radius (4px).
    *   [ ] Hover over a button. **Verify**: Background color changes (#0056b3).
    *   [ ] Click and hold a button. **Verify**: Background color changes (#004085).
    *   [ ] Observe disabled "Edit Task" / "Delete Task" buttons. **Verify**: Background color (#c0c0c0), text color (#808080).
*   [ ] **List Widget**:
    *   [ ] Check `QListWidget` border (1px solid #ccc), border-radius (4px), background (white).
    *   [ ] Check `QListWidget::item` padding (5px), bottom border (1px dotted #eee).
    *   [ ] Select an item. **Verify**: Background color (#007bff), text color (white).
    *   [ ] **Readability**: Ensure task titles are clearly readable.
    *   [ ] **Completed Tasks**: Ensure strikethrough on completed tasks is clear and doesn't obscure the title too much.
*   [ ] **Input Fields**:
    *   [ ] Check `QLineEdit` (in `TaskDialog`) padding (4px), border (1px solid #ccc), border-radius (4px).
*   [ ] **Radio Buttons**:
    *   [ ] Check spacing between radio button and its text label (5px).
*   [ ] **Dialog Appearance (`TaskDialog`)**:
    *   [ ] Open the "Add New Task" dialog.
    *   [ ] **Verify**: Background color is light gray (#f8f9fa or similar).
    *   [ ] **Usability**: Is the dialog easy to use? Is the input field clear? Are buttons distinct?
*   [ ] **Layout**:
    *   [ ] Observe the main action buttons ("Add", "Edit", "Delete"). **Verify**: They are grouped and pushed to the right due to a `QSpacerItem`.
    *   [ ] Observe the filter radio buttons ("All", "Active", "Completed"). **Verify**: They are grouped horizontally.
    *   [ ] **Overall**: Does the layout seem balanced and user-friendly?

---

**Additional Notes:**
*   Record any unexpected behavior, crashes, or visual glitches.
*   Note down the specific steps if a bug is found.
*   If possible, test on different screen resolutions or with different system themes to check adaptability (though this is advanced).
