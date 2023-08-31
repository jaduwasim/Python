from flask import Flask 

app = Flask(__name__)
@app.route('/home')
def home():
	return '<h1>Hello World!! This Respone form flask Application</h1>'

app.run(port=8000, debug=True)