@echo off
echo Installing required packages...
pip install -r requirements.txt

echo Building the application...
pyinstaller todo_app.spec

echo Done! The application has been built in the dist/TodoApp directory.
pause
