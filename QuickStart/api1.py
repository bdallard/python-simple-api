from flask import jsonify, Flask

app = Flask(__name__)

book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',

	}
]

@app.route('/')
def home():
	return "Hello World"


@app.route('/api/books', methods=["GET"])
def get_book():
	return jsonify({"book":book})

@app.route('/api/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
	b = [books for books in book if books['id'] == id]
	return jsonify({'books':b})

if __name__ == '__main__':
	app.run(debug=True)

