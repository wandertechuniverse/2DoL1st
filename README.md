# To-Do List Application

A simple, responsive to-do list application built with Flask and SQLite. The application can be run as a web app.

## Features

- Create, toggle, and delete tasks
- Filter tasks by status (All, Active, Completed)
- Responsive design that works on mobile and desktop
- Persistent storage using SQLite database

## Screenshots

![2DoL1st Home Page](https://raw.githubusercontent.com/wandertechuniverse/2DoL1st/refs/heads/master/2DoL1st%20Page.png)
![2DoL1st Active Tasks](https://raw.githubusercontent.com/wandertechuniverse/2DoL1st/refs/heads/master/2DoL1st%20Active%20Page.png)
![2DoL1st Completed Tasks](https://raw.githubusercontent.com/wandertechuniverse/2DoL1st/refs/heads/master/2DoL1st%20Completed%20Page.png)

## Installation

To get the application up and running, follow these steps:

1.  **Clone the repository:**
    Open your terminal or command prompt and run:
    ```bash
    git clone https://github.com/wandertechuniverse/2DoL1st.git
    cd 2DoL1st
    ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3.  **Install the required packages:**
    With the virtual environment activated, install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running as a Web Application

1.  **Ensure your virtual environment is active.** If not, activate it using the commands from the Installation section.
2.  **Run the Flask application:**
    ```bash
    python app.py
    ```
3.  **Access the application:**
    Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Project Structure

```
flask-todo-app/
├── app.py                  # Main application file
├── todo.db                 # SQLite database
├── requirements.txt        # Project dependencies
├── templates/              # HTML templates
│   └── index.html          # Main template
├── README.md              # Project documentation
└── LICENSE                # MIT License file
```

## How It Works

### Web Application
- The application uses Flask as the web framework
- Data is stored in a SQLite database
- The front-end is built with HTML, CSS, and minimal JavaScript
- Tasks can be filtered by their completion status

## Troubleshooting

Encountering issues? Here are some common problems and solutions:

* **`python: command not found` or `pip: command not found`**:
    * Ensure Python is installed and in your system's PATH
    * Verify by running `python --version`

* **Virtual environment issues**:
    * Double-check activation command: `.venv\Scripts\activate`
    * Ensure you're in the correct directory

* **Database errors**:
    * The `todo.db` file is created automatically on first run
    * Ensure write permissions in the application directory

## Future Improvements

- Add user authentication
- Add due dates for tasks
- Add categories/tags for tasks
- Implement task search functionality
- Add dark mode toggle

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask - Web framework
- SQLite - Database
- Font Awesome - Icons (if used)
