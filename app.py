from flask import Flask, request, jsonify, send_from_directory
import sqlite3

app = Flask(__name__)
DB = "tasks.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

# Create table if not exists
conn = get_db()
conn.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed INTEGER DEFAULT 0
)
""")
conn.commit()
conn.close()


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])


@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    conn = get_db()
    cursor = conn.execute(
        "INSERT INTO tasks (title, completed) VALUES (?, ?)",
        (data.get("title"), 0)
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": task_id, "title": data.get("title"), "completed": 0}), 201


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted"})


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    conn = get_db()
    conn.execute(
        "UPDATE tasks SET title = ?, completed = ? WHERE id = ?",
        (data.get("title"), data.get("completed"), task_id)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Task updated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
