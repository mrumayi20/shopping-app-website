from flask import Flask, render_template, jsonify
from database import load_clothing_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html')


@app.route("/clothing")
def clothing():
  clothings = load_clothing_from_db()
  return render_template('clothing.html', clothings=clothings)


# @app.route("/clothing")
# def clothing():
#   return jsonify(ITEMS)  #jsonift converts your data into JSON format

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
