import sqlite3
import os

DB_PATH = 'todo.db'

def init_db():
    """
    Initializes the SQLite database.
    Creates the 'todo' table if it doesn't already exist.
    """
    if not os.path.exists(DB_PATH):
        # Ensure the directory for DB_PATH exists if it's not in the current dir
        # For this project, DB_PATH is 'todo.db', so it's in the current directory.
        # If DB_PATH were, e.g., 'data/todo.db', os.makedirs(os.path.dirname(DB_PATH), exist_ok=True) would be needed.
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

class Todo:
    """
    Represents a single to-do item and provides static methods
    for database interactions related to to-do items.
    """
    def __init__(self, id, title, complete, created_at):
        """
        Constructs a Todo item.
        
        Args:
            id (int): The unique identifier of the to-do item.
            title (str): The title or description of the to-do item.
            complete (bool): The completion status of the to-do item.
            created_at (str): The timestamp when the to-do item was created.
        """
        self.id = id
        self.title = title
        self.complete = complete
        self.created_at = created_at

    @staticmethod
    def get_all():
        """Retrieves all to-do items from the database, ordered by creation date."""
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row # Access columns by name
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todo ORDER BY created_at DESC")
        rows = cursor.fetchall()
        todos = [Todo(row['id'], row['title'], bool(row['complete']), row['created_at']) for row in rows]
        conn.close()
        return todos

    @staticmethod
    def get_active():
        """Retrieves all active (not completed) to-do items."""
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
        """Retrieves all completed to-do items."""
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
        """
        Retrieves a single to-do item by its ID.
        
        Args:
            todo_id (int): The ID of the to-do item to retrieve.
            
        Returns:
            Todo or None: The Todo object if found, otherwise None.
        """
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
        """
        Adds a new to-do item to the database.
        
        Args:
            title (str): The title of the new to-do item.
        """
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            # New tasks are always added as not complete (False)
            cursor.execute("INSERT INTO todo (title, complete) VALUES (?, ?)", (title, int(False)))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            if conn:
                conn.close()

    @staticmethod
    def update_complete(todo_id, complete):
        """
        Updates the completion status of a to-do item.
        
        Args:
            todo_id (int): The ID of the to-do item to update.
            complete (bool): The new completion status (True for complete, False for active).
        """
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
            if conn:
                conn.close()

    @staticmethod
    def update_title(todo_id, new_title):
        """
        Updates the title of a to-do item.
        
        Args:
            todo_id (int): The ID of the to-do item to update.
            new_title (str): The new title for the to-do item.
        """
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("UPDATE todo SET title = ? WHERE id = ?", (new_title, todo_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            if conn:
                conn.close()

    @staticmethod
    def delete(todo_id):
        """
        Deletes a to-do item from the database.
        
        Args:
            todo_id (int): The ID of the to-do item to delete.
        """
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
            if conn:
                conn.close()

if __name__ == '__main__':
    # This block provides a basic test suite for the data_manager module.
    # It demonstrates the usage of each database operation.
    init_db()
    print("Database initialized for testing.")

    # Test: Add a new todo
    Todo.add("Test Todo from data_manager")
    print("Added 'Test Todo from data_manager'")

    # Test: Retrieve all todos
    all_todos = Todo.get_all()
    print(f"All todos after add: {[(todo.title, todo.complete) for todo in all_todos]}")

    # Test: Retrieve active todos
    active_todos = Todo.get_active() # Should contain the new test todo
    print(f"Active todos: {[(todo.title, todo.complete) for todo in active_todos]}")

    # Test: Retrieve completed todos
    completed_todos = Todo.get_completed()
    print(f"Completed todos (should be empty): {[(todo.title, todo.complete) for todo in completed_todos]}")

    # Test: Update operations (title and completion)
    if active_todos:
        # Get the ID of the task we just added (assuming it's the first in active_todos)
        task_to_update_id = active_todos[0].id
        original_title = active_todos[0].title

        # Test: Update title
        new_title_for_test = f"Updated Title for {original_title}"
        Todo.update_title(task_to_update_id, new_title_for_test)
        print(f"Updated title for task ID {task_to_update_id} to '{new_title_for_test}'")
        updated_todo_for_title_check = Todo.get_by_id(task_to_update_id)
        if updated_todo_for_title_check:
            print(f"Verified updated title: {updated_todo_for_title_check.title}")
        else:
            print(f"Error: Task with ID {task_to_update_id} not found after title update.")


        # Test: Update completion status
        Todo.update_complete(task_to_update_id, True) # Mark as complete
        print(f"Marked task '{new_title_for_test}' (ID: {task_to_update_id}) as complete.")
        updated_todo_for_completion_check = Todo.get_by_id(task_to_update_id)
        if updated_todo_for_completion_check:
            print(f"Verified updated completion status: {updated_todo_for_completion_check.complete}")
        else:
            print(f"Error: Task with ID {task_to_update_id} not found after completion update.")
        
        # Test: Retrieve completed todos again
        completed_todos_after_update = Todo.get_completed()
        print(f"Completed todos after update: {[(todo.title, todo.complete) for todo in completed_todos_after_update]}")

        # Test: Delete the task
        print(f"Attempting to delete task '{new_title_for_test}' (ID: {task_to_update_id}).")
        Todo.delete(task_to_update_id)
        deleted_todo_check = Todo.get_by_id(task_to_update_id)
        if deleted_todo_check is None:
            print(f"Task with ID {task_to_update_id} successfully deleted.")
        else:
            print(f"Error: Task with ID {task_to_update_id} not deleted. Current title: {deleted_todo_check.title}")
    else:
        print("No active todos found to test update and delete operations.")
    
    # Final check: Ensure the database is clean for subsequent runs if necessary, or list remaining.
    remaining_todos = Todo.get_all()
    print(f"Remaining todos after all tests: {[(todo.title, todo.complete) for todo in remaining_todos]}")
    print("Test suite finished.")
