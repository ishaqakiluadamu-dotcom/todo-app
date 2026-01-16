from flask import Flask, request, jsonify

app = Flask(__name__)

# Tasks stored in-memory for simplicity
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    if not task:
        return jsonify({"error": "Task is required"}), 400
    tasks.append(task)
    return jsonify({"message": "Task added", "task": task}), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        removed = tasks.pop(task_id)
        return jsonify({"message": "Task deleted", "task": removed})
    else:
        return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
