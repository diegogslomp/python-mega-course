from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from sqlalchemy.sql import func

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://uatxhawyshdxya:9379c71afbe21b6f943e95511262fbbe372bf2c155e2ad22b8a8468b40dd1e24@ec2-107-22-241-243.compute-1.amazonaws.com:5432/dbbe6hbfsua6ne?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email=request.form['email']
        height=request.form['height']
        if db.session.query(Data).filter(Data.email==email).count() == 0:
            data=Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = round(db.session.query(func.avg(Data.height)).scalar())
            count = db.session.query(Data.height).count()
#            send_mail(email, height, average_height, count)
            return render_template('success.html')
        return render_template('index.html', message="Email already in database!")

if __name__ == '__main__':
    app.debug=True
    app.run(host = '0.0.0.0')
    app.run()
