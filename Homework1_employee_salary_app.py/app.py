from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'employee_data'

mysql = MySQL(app)

@app.route("/", methods=["POST","GET"])
def index():
    msg = ""
    if request.method=="POST":
        name = request.form["name"]
        id = request.form["id"]
        salary = float(request.form["salary"])

        action = request.form.get("action")

        if action == "submit":
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO employee_salary(employee_name, employee_id, salary) VALUES(%s, %s, %s)", (name,id,salary))
            mysql.connection.commit()
            cur.close()

            
            msg = f"{name} your data was inserted successfully"
        elif action == "increasesalary":
            increased_salary = salary * 1.05
        
            msg = f"""
            Employee Salary Increase<br>
            Employee Name: {name}<br>
            Employee ID: {id}<br>
            Employee Salary: {salary:.0f}<br>
            The increase salary is $ {increased_salary:.2f}
            """
    return render_template('index_Evan_Dong.html', msg = msg)

if __name__ == "__main__":
    app.run(debug=True)