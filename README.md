# Flask To-Do List Application

A simple, responsive to-do list application built with Flask and SQLite. The application can be run as a web app.

## Features

- Create, toggle, and delete tasks
- Filter tasks by status (All, Active, Completed)
- Responsive design that works on mobile and desktop
- Persistent storage using SQLite database

## Screenshots

![To-Do List App](screenshots/todo-app.png)

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

## Project Structure

```
flask-todo-app/
├── app.py                  # Main application file
├── todo_app.spec           # PyInstaller specification file
├── todo.db                 # SQLite database
├── requirements.txt        # Project dependencies
├── templates/              # HTML templates
│   └── index.html          # Main template
├── README.md               # Project documentation
└── LICENSE                 # MIT License file
```

## How It Works

### Web Application
- The application uses Flask as the web framework
- Data is stored in a SQLite database
- The front-end is built with HTML, CSS, and minimal JavaScript
- Tasks can be filtered by their completion status

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

Copyright (c) 2023 To-Do List App

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
````
