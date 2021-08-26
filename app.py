from flask import Flask, render_template
import mysql.connector

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


if __name__=='__main__':
    app.run(debug=True)

