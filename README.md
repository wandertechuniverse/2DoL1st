# To-Do List Application

A simple, responsive to-do list application built with Flask and SQLite. The application can be run as a web app or packaged as a standalone desktop application for Windows, macOS, and Linux.

## Features

- Create, toggle, and delete tasks
- Filter tasks by status (All, Active, Completed)
- Responsive design that works on mobile and desktop
- Persistent storage using SQLite database
- Can be packaged as a standalone desktop application

## Screenshots

![To-Do List App](screenshots/todo-app.png)

## Installation

To get the application up and running, follow these steps:

1.  **Clone the repository:**
    Open your terminal or command prompt and run:
    ```bash
    git clone https://github.com/wandertechuniverse/2DoL1st.git
    cd 2DoL1st
    ```

2.  **Create a virtual environment and activate it:**
    It's recommended to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv .venv
    ```
    * On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

3.  **Install the required packages:**
    With the virtual environment activated, install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can use the application either as a web application or build it into a standalone desktop application.

### Running as a Web Application

1.  **Ensure your virtual environment is active.** If not, activate it using the commands from the Installation section.
2.  **Run the Flask application:**
    ```bash
    python app.py
    ```
3.  **Access the application:**
    Open your web browser and navigate to:
    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```
    You should see the To-Do List interface.

### Building as a Desktop Application

This method uses PyInstaller and PyWebView to create a standalone executable.

1.  **Ensure your virtual environment is active** and you have installed the packages from `requirements.txt`, which includes `pyinstaller` and `pywebview`.
2.  **Run the build script:**

    * **On Windows:**
        Open command prompt in the project directory and run:
        ```batch
        build_app.bat
        ```

    * **On macOS/Linux:**
        Open terminal in the project directory. First, make the script executable:
        ```bash
        chmod +x build_app.sh
        ```
        Then run the script:
        ```bash
        ./build_app.sh
        ```
3.  **Locate the standalone application:**
    After the build process completes (which may take a few minutes), the standalone application will be created in the `dist/` directory. The exact location will be `dist/TodoApp`.

4.  **Run the desktop application:**

    * **On Windows:**
        Navigate to the `dist/TodoApp` directory and double-click on `TodoApp.exe`.

    * **On macOS:**
        Navigate to the `dist` directory and double-click on `TodoApp.app`.

    * **On Linux:**
        Navigate to the `dist/TodoApp` directory and run `./TodoApp` in your terminal.

## Project Structure

```
flask-todo-app/
├── app.py                  # Main Flask application file
├── desktop_app.py          # Simple desktop wrapper using webbrowser (alternative/deprecated)
├── webview_app.py          # Advanced desktop wrapper using pywebview (used for build)
├── todo_app.spec           # PyInstaller specification file for building
├── build_app.bat           # Windows build script (calls PyInstaller)
├── build_app.sh            # macOS/Linux build script (calls PyInstaller)
├── todo.db                 # SQLite database file (created on first run if not exists)
├── requirements.txt        # Project dependencies list
├── templates/              # HTML templates directory
│   └── index.html          # Main application template
├── README.md               # Project documentation (this file)
└── LICENSE                 # MIT License file
```

## How It Works

### Web Application
- The core application logic is handled by **Flask**, a Python web framework.
- **SQLite** is used as the database engine for persistent storage of tasks. The `todo.db` file stores all your to-do items.
- The user interface is built using standard web technologies: **HTML**, **CSS**, and minimal **JavaScript** for dynamic interactions like toggling task status.
- Flask routes handle requests to display tasks, add new tasks, toggle status, delete tasks, and filter the view.

### Desktop Application
- The desktop version leverages **PyWebView** to embed a web browser component (utilizing the native system's web rendering engine) within a standalone application window.
- **PyInstaller** is used to package the Python code (Flask app, PyWebView wrapper), templates, static files (if any), and the SQLite database into a single executable directory or file.
- When the desktop application starts, it internally runs the Flask development server on a local port (usually ephemeral), and PyWebView opens a window pointed to `http://127.0.0.1:<port>/`.
- This means the desktop application is essentially running the web app locally in a dedicated window, providing a native feel while using the same Flask backend and SQLite database.
- All data remains stored locally in the `todo.db` file within the application's data directory.

## Troubleshooting

Encountering issues? Here are some common problems and solutions:

* **`python: command not found` or `pip: command not found`**:
    * Ensure Python is installed on your system and is included in your system's PATH. You might need to restart your terminal or computer after installation.
    * Verify Python installation by running `python --version` or `python3 --version`.

* **Virtual environment activation issues**:
    * Double-check the commands for activating the virtual environment (`.venv\Scripts\activate` for Windows, `source .venv/bin/activate` for macOS/Linux).
    * Ensure you are in the correct project directory (`cd 2DoL1st`) before attempting to activate.

* **`pip install -r requirements.txt` fails**:
    * Make sure your virtual environment is active. Installations should happen within the virtual environment.
    * Check for specific error messages during installation. Some libraries might require system-level dependencies (less common for Flask/SQLite, but possible).
    * Ensure your internet connection is stable to download packages from PyPI.

* **Web application doesn't start (`python app.py`)**:
    * Look at the error messages in the terminal. They usually indicate the cause, such as missing modules (`ModuleNotFoundError`) or errors in the code.
    * Ensure you have installed packages from `requirements.txt` within the active virtual environment.
    * Check if another process is already using port 5000. You might see an error like `Address already in use`. You can try stopping the other process or modifying `app.py` to use a different port.

* **Database file (`todo.db`) not found or errors**:
    * The `todo.db` file is automatically created by Flask-SQLAlchemy when the application runs for the first time and the database connection is attempted.
    * Ensure the application has write permissions in the directory where `app.py` is located.
    * If you're running the desktop app, the database file will be located within the data directory of the packaged application (usually in a user's application data folder, location varies by OS and PyInstaller settings). Errors here often relate to permissions or packaging issues.

* **Desktop application build fails (`build_app.bat`/`build_app.sh`)**:
    * Read the output from PyInstaller carefully. It will often point to missing files, syntax errors in the `.spec` file, or issues finding dependencies.
    * Ensure `pyinstaller` is installed in your active virtual environment.
    * Check permissions on the build scripts (`chmod +x build_app.sh` on macOS/Linux).
    * Building can sometimes be sensitive to the Python version or OS environment. Ensure you are using a supported environment.

* **Desktop application runs but shows a blank window or connection error**:
    * This often means the internal Flask server failed to start or the PyWebView window couldn't connect to it.
    * Check the console output of the standalone application (if running from terminal) for errors from Flask or PyWebView.
    * Ensure the `webview_app.py` script is correctly starting the Flask server in a separate thread or process.

If you encounter an issue not listed here, please refer to the specific error message you receive, which is the most helpful guide to the underlying problem.

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

Copyright (c) 2025 2DoL1st App

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

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [SQLite](https://www.sqlite.org/index.html) - Database
- [PyWebView](https://pywebview.flowrl.com/) - Python library to build GUI for web applications
- [PyInstaller](https://pyinstaller.org/) - Tool to package Python programs into standalone executables
- [Font Awesome](https://fontawesome.com/) - Icons (if used)
