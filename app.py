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

@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
 
    data = request.get_json(silent=True)
 
    if data is None:
        return jsonify({"error": "Please send JSON data"}), 400
 
    title = data.get("title")
 
    if not title or not isinstance(title, str) or title.strip() == "":
        return jsonify({"error": "'title' is required and cannot be empty"}), 400
 
    new_task = {
        "title": title.strip(),
        "done": False
    }
 
    tasks[next_id] = new_task
    new_task_id = next_id
    next_id += 1  
 
    return jsonify({"id": new_task_id, **new_task}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = tasks.get(task_id)
 
    if task is None:
        return jsonify({"error": "Task not found"}), 404
 
    data = request.get_json(silent=True)
 
    if data is None:
        return jsonify({"error": "Please send JSON data"}), 400
 
    if "title" in data:
        title = data["title"]
        if not title or not isinstance(title, str) or title.strip() == "":
            return jsonify({"error": "'title' cannot be empty"}), 400
        task["title"] = title.strip()
 
    if "done" in data:
        if not isinstance(data["done"], bool):
            return jsonify({"error": "'done' must be true or false"}), 400
        task["done"] = data["done"]
 
    return jsonify(task)

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = tasks.get(task_id)
 
    if task is None:
        return jsonify({"error": "Task not found"}), 404
 
    del tasks[task_id]
 
    return jsonify({"message": "Task deleted"}), 200