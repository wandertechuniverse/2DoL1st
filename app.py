from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DB_PATH = 'todo.db'

# Create the database if it doesn't exist
def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            complete BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        conn.commit()
        conn.close()

init_db()

# Todo class to represent a todo item
class Todo:
    def __init__(self, id, title, complete, created_at):
        self.id = id
        self.title = title
        self.complete = complete
        self.created_at = created_at

    @staticmethod
    def get_all():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todo ORDER BY created_at DESC")
        rows = cursor.fetchall()
        todos = [Todo(row['id'], row['title'], bool(row['complete']), row['created_at']) for row in rows]
        conn.close()
        return todos

    @staticmethod
    def get_active():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todo WHERE complete = 0 ORDER BY created_at DESC")
        rows = cursor.fetchall()
        todos = [Todo(row['id'], row['title'], bool(row['complete']), row['created_at']) for row in rows]
        conn.close()
        return todos

    @staticmethod
    def get_completed():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todo WHERE complete = 1 ORDER BY created_at DESC")
        rows = cursor.fetchall()
        todos = [Todo(row['id'], row['title'], bool(row['complete']), row['created_at']) for row in rows]
        conn.close()
        return todos

    @staticmethod
    def get_by_id(todo_id):
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todo WHERE id = ?", (todo_id,))
        row = cursor.fetchone()
        todo = Todo(row['id'], row['title'], bool(row['complete']), row['created_at']) if row else None
        conn.close()
        return todo

    @staticmethod
    def add(title):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO todo (title, complete) VALUES (?, ?)", (title, int(False)))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_complete(todo_id, complete):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("UPDATE todo SET complete = ? WHERE id = ?", (int(complete), todo_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete(todo_id):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todo WHERE id = ?", (todo_id,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            conn.close()

@app.route('/')
@app.route('/all')
def index():
    todo_list = Todo.get_all()
    active_tab = 'all'
    return render_template('index.html', todo_list=todo_list, active_tab=active_tab)

@app.route('/active')
def active():
    todo_list = Todo.get_active()
    active_tab = 'active'
    return render_template('index.html', todo_list=todo_list, active_tab=active_tab)

@app.route('/completed')
def completed():
    todo_list = Todo.get_completed()
    active_tab = 'completed'
    return render_template('index.html', todo_list=todo_list, active_tab=active_tab)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        Todo.add(title)
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>')
@app.route('/update/<int:todo_id>/<string:redirect_to>')
def update(todo_id, redirect_to='all'):
    todo = Todo.get_by_id(todo_id)
    if todo:
        Todo.update_complete(todo_id, not todo.complete)
    if redirect_to == 'active':
        return redirect(url_for('active'))
    elif redirect_to == 'completed':
        return redirect(url_for('completed'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
@app.route('/delete/<int:todo_id>/<string:redirect_to>')
def delete(todo_id, redirect_to='all'):
    todo = Todo.get_by_id(todo_id)
    if todo:
        Todo.delete(todo_id)
    if redirect_to == 'active':
        return redirect(url_for('active'))
    elif redirect_to == 'completed':
        return redirect(url_for('completed'))
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)