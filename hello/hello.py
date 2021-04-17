from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hi/')
@app.route('/hi/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

if __name__ == '__main__':
	app.run(debug=True)

# https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
