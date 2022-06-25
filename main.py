from flask import Flask, redirect, url_for, render_template, request
from retrieve_data import RetrieveData

stretches_dict={}
def populate_stretches_dict():
    for line in open("stretch_descriptions.txt","r"):
        values=line.split(':')
        try:
            if line.index("\n") != -1:
                values[1]=values[1][0:len(values[1])-1]
            stretches_dict[str(values[0])]=str(values[1])
        except Exception as e:
            stretches_dict[str(values[0])]=str(values[1])

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ved"
    return app

app = create_app()
populate_stretches_dict()

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
    stretch_names=parse_muscles(viable_stretches)

    try:
        group=group.replace("_"," ")
    except Exception as e:
        print(e)
    return render_template("content.html", muscle_group=str(group).upper(), names=stretch_names, stretchesArr=stretches_lst)

def parse_rows(rows):
    arrTemplate=[]
    desc_lst=[]

    for index in rows:
        arrTemplate.append(index[0])

    for stretches in arrTemplate:
        desc_lst.append(stretches_dict[str(stretches)])
    
    return desc_lst

def parse_muscles(rows):
    arrTemplate=[]
    for index in rows:
        stretchName=""
        try:
            stretchName=index[0].replace("'","")
        except Exception as e:
            stretchName=index[0]

        try:
            stretchName=stretchName.replace(" ","_")
        except Exception as e:
            stretchName=stretchName
        arrTemplate.append(stretchName)
    return arrTemplate

if __name__ == "__main__":
    app.run(debug=True)