from flask import Flask, render_template, request
import mysql.connector
from werkzeug.exceptions import RequestEntityTooLarge

config = {
  'user': 'root',
  'password': 'root',
  'host': 'db',
  'port': '3306',
  'database': 'feedback',
  'raise_on_warnings': True
}

# cnx = mysql.connector.connect(**config)

# cnx.close()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def insertFeedback(name, email, feedback):
    sql = ""
    sql +="INSERT INTO "

@app.route('/', methods = ["POST", "GET"])
def takeFeedback():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        feedback = request.form["feedback"]

        print("{} \n {} \n {}".format(name, email, feedback))
        return render_template('index.html', anchor="contact")

if __name__=='__main__':
    app.run(debug=True)

