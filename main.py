import smtplib
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email
import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    headline = db.Column(db.Text)
    description = db.Column(db.Text)
    footage = db.Column(db.Text)
    image = db.Column(db.Text)

def __init__(self, title, headline, description, footage, image):
    self.title = title
    self.headline = headline
    self.description = description
    self.footage = footage
    self.image = image


def __repr__(self):
    return "Nothing"

app.config['SECRET_KEY'] = 'jeremygu'

class InfoForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    email = EmailField("Email address: ", validators = [DataRequired(), Email()])
    subject = StringField("Subject: ", validators = [DataRequired()])
    message = TextAreaField("Message: ", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/footages')
def footages():
    blogs = Blog.query.all()
    return render_template("footages.html", blogs=blogs)

@app.route('/follow')
def follow():
    return render_template("follow.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    from_addrs = "notabotz1776@gmail.com"
    to_addrs = "notabotz1776@gmail.com"
    password = "cjwdinrxvtywwiib"
    message = ''
    form = InfoForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['subject'] = form.subject.data
        session['message'] = form.message.data
        # message = "Name: " + form.name.data + "Email: " + form.email.data + "Message: " + form.message.data
        message = f"Subject: {form.name.data + " " + form.subject.data}\n\n EmaiL: {form.email.data} \n\nMessage: {form.message.data}"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(from_addrs, password)
            for i in range(1):
                connection.sendmail(from_addrs, to_addrs, message)

        return redirect(url_for('thankyou'))
    # else:
    #     return redirect(url_for('error'))

    return render_template("contact.html", form=form)
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")

@app.errorhandler(404)
def invalid_route(e):
    return "Page Not Found"
if __name__ == '__main__':
    app.run(debug=True)
