from flask import Flask , request , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:aslongasyou@localhost/flask_books'

db = SQLAlchemy(app)


class Books(db.Model):
	name = db.Column(db.String(30),primary_key=True)
	score = db.Column(db.Integer)
	review = db.Column(db.String(150))


	def __init__(self,name,score,review):
		self.name = name
		self.score = score
		self.review = review

	def __repr__(self):
		return self.name



@app.route('/submit',methods=['POST','GET'])
def submit():
	if request.method == 'POST':
		name = request.form['name']
		score= request.form['score']
		review = request.form['review']
		print(name,score,review)
		if db.session.query(Books).filter(Books.name == name).count()==0:		
			data = Books(name,score,review)
			db.session.add(data)
			db.session.commit()
			return render_template('success.html')
		return render_template('index.html')
	if request.method == 'GET':
		return render_template('index.html')


if __name__ == "__main__":
	app.run()