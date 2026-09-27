from flask import Flask, request, jsonify
 
app = Flask(__name__)

tasks = {}
next_id = 1 

@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    return jsonify(tasks)

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_one_task(task_id):
    task = tasks.get(task_id)
 
    if task is None:
        return jsonify({"error": "Task not found"}), 404
 
    return jsonify(task)