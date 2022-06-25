from ast import parse
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
    # Initiate connection thru object
    conn = RetrieveData()
    conn.connect()

    # Retrieve necessary rows
    viable_stretches=conn.check_stretches(group)
    muscles=conn.check_muscles(group)

    conn.close_connection() #close connection

    stretches_lst=parse_rows(viable_stretches)
    return render_template("content.html", stretchesArr=stretches_lst)

def parse_rows(rows):
    arrTemplate=[]
    for index in rows:
        arrTemplate.append(index[0])
    return arrTemplate

if __name__ == "__main__":
    app.run(debug=True)