from flask import Flask, redirect, render_template, request
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("database.db")
db.cursor().execute(
    """
CREATE TABLE IF NOT EXISTS employee(
id INTEGER PRIMARY KEY ,
name TEXT,
salary INTEGER
)
"""
)
db.commit()
db.close()


@app.route("/")
def home():
    db = sqlite3.connect("database.db")
    employees = (
        db.cursor().execute("SELECT id,name,salary FROM employee").fetchall()
    )
    db.close()
    return render_template("index.html", employees=employees)


@app.route("/add", methods=["GET", "POST"])
def add():
    Name = request.form["Name"]
    Salary = request.form["Salary"]
    db = sqlite3.connect("database.db")
    db.cursor().execute(
        "INSERT INTO employee (Name,Salary) VALUES(?,?)", (Name, Salary)
    )
    db.commit()
    db.close()
    return redirect("/")


@app.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    db = sqlite3.connect("database.db")
    db.cursor().execute("DELETE FROM employee WHERE id = ?", (id,))
    db.commit()
    db.close()
    return redirect("/")


@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    Name = request.form["Name"]
    Salary = request.form["Salary"]
    db = sqlite3.connect("database.db")
    db.cursor().execute(
        "UPDATE employee SET Name = ? , Salary = ? WHERE ID = ?",
        (Name, Salary, id),
    )
    db.commit()
    db.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)