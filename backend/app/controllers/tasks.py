from flask import request, jsonify
from app import create_app, db
from app.models import Task

app = create_app()

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if request.method == 'GET':
        tasks = Task.query.all()
        return jsonify([{'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed} for task in tasks]), 200
    # Add POST logic here

# Add more routes here