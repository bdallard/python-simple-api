from flask import jsonify, Flask
import json 

app = Flask(__name__)

#load json 
with open('./data/books.json') as f:
	books = json.load(f)

@app.route('/')
def home():
	return "Hello this is an API crash course"

@app.route('/api/books', methods=["GET"])
def get_book():
	return jsonify({"books":books})


@app.route('/api/books/<string:title>', methods=["GET"])
def get_book_title(title):
	book = [book for book in books if books['title']==title]
	return jsonify({"Books":book})

if __name__ == '__main__':
	app.run(debug=True)
