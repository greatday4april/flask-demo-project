from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)
db.create_all()


@app.route('/table/')
def table():
    users = User.query
    return render_template("basic_table.html", title='Basic Table', users=users)


if __name__ == '__main__':
    app.debug = True
    app.run()
