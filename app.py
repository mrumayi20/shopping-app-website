from flask import Flask, render_template, jsonify

app = Flask(__name__)

ITEMS =[
  {
    'id': 1,
    'title': 'Shirt',
    'price': '10',
    'rating': 4.5
  },
  {
    'id': 2,
    'title': 'Watch',
    'price': '50',
    'rating': 4
  },
  {
    'id': 3,
    'title': 'Shoe',
    'price': '35',
    'rating': 5
  },
  {
    'id': 4,
    'title': 'Shoe',
    'price': '35',
    'rating': 5
  },
  {
    'id': 5,
    'title': 'Shoe',
    'price': '35',
    'rating': 5
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html')

# @app.route("/clothing")
# def clothing():
#   return render_template('clothing.html', items=ITEMS)

@app.route("/clothing")
def clothing():
  return jsonify(ITEMS)#jsonift converts your data into JSON format
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
