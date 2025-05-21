# Flask To-Do List Application

A simple, responsive to-do list application built with Flask and SQLite. The application can be run as a web app.

## Features

- Create, toggle, and delete tasks
- Filter tasks by status (All, Active, Completed)
- Responsive design that works on mobile and desktop
- Persistent storage using SQLite database
- Can be packaged as a standalone desktop application

## Screenshots

### Flask Web Application
![To-Do List App - Web Version](screenshots/todo-app.png)

### Qt Desktop Application
The following screenshots are for the `desktop_qt_app.py` application.

![Main View](2DoL1st%20Page.png)
*Main view of the Qt desktop application showing all tasks.*

![Active Tasks](2DoL1st%20Active%20Page.png)
*View showing only active tasks in the Qt desktop application.*

![Completed Tasks](2DoL1st%20Completed%20Page.png)
*View showing only completed tasks in the Qt desktop application.*

## Installation

1. Clone the repository:
   
   ```
   git clone https://github.com/yourusername/flask-todo-app.git
   cd flask-todo-app
   ```

2. Create a virtual environment and activate it:
   
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install the required packages:
   
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running as a Web Application

1. Run the application:
   
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   
   ```
   http://127.0.0.1:5000/
   ```

## Desktop Application (`desktop_qt_app.py`)

This project also includes a native desktop To-Do List application built using Python and the Qt framework with the PySide6 bindings.

**Key Features:**
-   **Full To-Do Management**: Create, edit, delete, and mark tasks as complete or active.
-   **Task Filtering**: View all, active, or completed tasks.
-   **Native Notifications**: Receive system notifications when tasks are added or completed.
-   **System Tray Integration**: The application can minimize to the system tray and provides quick actions (show app, quit) from the tray icon menu.

**Dependencies:**
The primary dependency for the desktop application is:
-   `PySide6` (for the Qt GUI framework)
-   `Pillow` (for creating the placeholder tray icon, optional if you provide your own)

**Running the Desktop Application:**
First, ensure you have cloned the repository and navigated into its main directory (e.g., `2DoL1st` if you used the default clone name).
1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the application:
    ```bash
    python desktop_qt_app.py
    ```
    The application window should appear. If you have a compatible system tray, an icon will appear there.

**Manual Testing:**
For detailed steps on how to manually test all features of the desktop application, please refer to the `MANUAL_TESTING_CHECKLIST.md` file in this repository.

### Original Flask Web App - Building as a Desktop Application (Legacy PyWebView version)

1. Install the required packages:
   
   ```
   pip install -r requirements.txt
   ```

2. Build the application:
   
   **On Windows:**
   
   ```
   build_app.bat
   ```
   
   **On macOS/Linux:**
   
   ```
   chmod +x build_app.sh
   ./build_app.sh
   ```

3. The standalone application will be available in the `dist/TodoApp` directory.

4. To run the application:
   
   **On Windows:**
   
   - Navigate to `dist/TodoApp` and double-click on `TodoApp.exe`
   
   **On macOS:**
   
   - Navigate to `dist` and double-click on `TodoApp.app`
   
   **On Linux:**
   
   - Navigate to `dist/TodoApp` and run `./TodoApp`

## Project Structure

```
flask-todo-app/
├── app.py                  # Main Flask web application file
├── data_manager.py         # Handles database interactions for both apps
├── desktop_qt_app.py       # Qt-based desktop application
├── MANUAL_TESTING_CHECKLIST.md # Checklist for testing desktop_qt_app.py
├── PACKAGING_NOTES.md      # Notes on packaging the Qt desktop application
├── tray_icon.png           # Placeholder icon for system tray
├── todo.db                 # SQLite database (shared by both apps)
├── requirements.txt        # Project dependencies (for both apps)
├── templates/              # HTML templates (for Flask app)
│   └── index.html          # Main template for Flask app
├── README.md               # Project documentation
└── LICENSE                 # MIT License file
# Older files for PyWebView desktop app (may be outdated or removed):
# desktop_app.py
# webview_app.py
# todo_app.spec
# build_app.bat
# build_app.sh
```

## How It Works

### Web Application

- The application uses Flask as the web framework
- Data is stored in a SQLite database
- The front-end is built with HTML, CSS, and minimal JavaScript
- Tasks can be filtered by their completion status

### Desktop Application

- The desktop version uses PyWebView to create a native window
- PyWebView embeds a web browser component to display the Flask application
- PyInstaller packages everything into a standalone executable
- The application runs a local Flask server and connects to it via the embedded browser
- All data is stored locally in the SQLite database

## Future Improvements

- Add user authentication
- Add due dates for tasks
- Add categories/tags for tasks
- Implement task search functionality
- Add dark mode toggle

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 To-Do List App

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Acknowledgements

- Flask - Web framework
- SQLite - Database
- Font Awesome - Icons (if used)

© 2025 2DoL1st
