from flask import Flask 

app = Flask(__name__)
@app.route('/home')
def home():
	return '<h1>Hello World!! This Respone form flask Application</h1>'

app.run(port=8000, debug=True)

# from flask import Flask, render_template

# app = Flask(__name__)
# @app.route('/home')
# def home():
# 	return render_template('home.html')

# if __name__ == '__main__':
# 	app.run(port=8000, debug=True)