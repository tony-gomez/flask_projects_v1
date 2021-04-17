from peewee import *

db = SqliteDatabase('sqlite3.db')

class Question(Model):
	question_text = CharField()
	#pub_date = DateTimeField("date published")

	class Meta:
		database = db

	def __str__(self):
		return self.question_text




class Choice(Model):
	question = ForeignKeyField(Question, backref='choices')
	choice_text = CharField()
	votes = IntegerField(default=0)

	class Meta:
		database = db

	def __str__(self):
		return self.choice_text


def create_tables():
	with db:
		db.create_tables([Question, Choice])