from flask import Flask, redirect, url_for, render_template, request
from retrieve_data import RetrieveData

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ved"
    return app

app = create_app()

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/muscle-group=<group>')
def get_stretches(group):
    conn = RetrieveData()
    conn.connect()

    viable_stretches=conn.check_stretches(group)
    muscles=conn.check_muscles(group)

    conn.close_connection() #close connection

    return render_template("content.html", stretchesArr="overhead stretch")


if __name__ == "__main__":
    app.run(debug=True)