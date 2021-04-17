from flask import Flask, render_template, url_for, request, redirect
from models import Question, Choice

app = Flask(__name__)


@app.route('/')
def index():
	latest_question_list = Question.select()
	return render_template('index.html', latest_question_list=latest_question_list)


@app.route('/<int:question_id>/')
def detail(question_id):
	question = Question.get(id=question_id)
	return render_template('detail.html', question=question)


@app.route('/<int:question_id>/results/')
def results(question_id):
	question = Question.get(id=question_id)
	return render_template('results.html', question=question)



@app.route('/<int:question_id>/vote/', methods=['GET', 'POST'])
def vote(question_id):
	question = Question.get(id=question_id)


	selected_choice = question.choices.select().where(Choice.id==request.form.get('choice')).get()


	selected_choice.votes += 1
	selected_choice.save()

	return redirect(url_for('results', question_id=question.id))


if __name__ == '__main__':
	app.run(debug=True)