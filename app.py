from flask import Flask, render_template, request, redirect, url_for
from data_manager import Todo, init_db

app = Flask(__name__)

# Initialize the database
init_db()

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