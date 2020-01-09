from flask import Flask, render_template, request, jsonify
from palin import *
app = Flask(__name__)

@app.route('/',methods=['GET' , 'POST'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']

	if name :
		newName = findNextPalindrome(name)
		return jsonify({'name' : newName})

	return jsonify({'error' : 'No Input!'})

if __name__ == '__main__':
	app.run(debug=True)