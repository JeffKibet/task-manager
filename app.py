from flask import Flask, request, jsonify
 
app = Flask(__name__)

tasks = {}
next_id = 1 

@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    return jsonify(tasks)