from flask import Flask, render_template, request, jsonify
import mysql, mysql.connector

app = Flask(__name__)

#------------------------
# Database configuration
#------------------------
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "flaskuser"
app.config["MYSQL_PASSWORD"] = "password123"
app.config["MYSQL_DB"] = "todo_db"

# database connection
db = mysql.connector.connect(
    host = app.config["MYSQL_HOST"],
    user = app.config["MYSQL_USER"],
    password = app.config["MYSQL_PASSWORD"],
    database = app.config["MYSQL_DB"]
)

#------------------------
# homepage route
#------------------------
@app.route('/')
def index():
    return render_template("index.html")

#-----------------------
# get all tasks
#-----------------------
@app.route("/get_tasks", methods = ["GET"])
def get_task():
    try:
        with db.cursor(dictionary = True) as cursor:
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
        return jsonify(tasks)

    except mysql.connector.Error as e:
        return jsonify({"ERROR...": str(e)}), 500

#---------------------
# add new tasks
#---------------------
@app.route("/add_task", methods = ["POST"])
def add_task():
    data = request.get_json(silent=True) or {}
    task = data.get("task")

    if isinstance(task, str) and task.strip():
        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO tasks(task) VALUES (%s)", (task.strip(),))
            db.commit()
            cursor.close()
            return jsonify({"status": "Success"})
        except mysql.connector.Error as e:
            return jsonify({"ERROR...": str(e)}), 500

    return jsonify({"status": "Error with task"})

#-----------------
# delete a task
#-----------------
@app.route("/delete_task", methods = ["POST"])
def delete_task():
    data = request.get_json(silent=True) or {}
    task_id = data.get("id")

    if task_id is not None:
        try:
            cursor = db.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
            db.commit()
            cursor.close()
            return jsonify({"status": "Success"})
        except mysql.connector.Error as e:
            return jsonify({"ERROR...": str(e)}), 500

    return jsonify({"status": "Error with task"})


if __name__ == "__main__":
    app.run(debug=True)