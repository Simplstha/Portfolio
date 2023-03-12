from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("AppSecretKey")
Bootstrap(app)


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    message = StringField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Send Me as Email')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)