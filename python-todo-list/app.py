from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")

def homepage():
    task_list = List.query.all()
    return render_template("index.html", task_list=task_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_task = List(title=title, complete=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("homepage"))


@app.route("/update/<int:task_id>")
def update(task_id):
    task = List.query.filter_by(id=task_id).first()
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for("homepage"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = List.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("homepage"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
