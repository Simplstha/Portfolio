from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired
import os
import smtplib

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
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        my_email = os.getenv("MyEmail")
        password = os.getenv("MyPassword")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs="sharmisthashaw3@gmail.com",
                msg=f"Subject:Feedback from My Portfolio \n\nName = {name}\nEmail = {email}\nMessage = {message}"
            )
        return redirect(url_for("home"))
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)