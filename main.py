from flask import Flask, render_template, flash

app = Flask(__name__, template_folder="templates")
app.secret_key = "super secret key"


@app.route('/dashboard/')
def dashboard():
    flash("Now you should be able to use flash to pass a dismissable message")
    flash("This is the dismissable message")
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
