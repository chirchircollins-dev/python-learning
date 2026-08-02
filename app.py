from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=100)])
    phone_number = StringField("Phone Number", validators=[DataRequired(), Length(min=10, max=20)])
    submit = SubmitField("Add Contact")

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(name=form.name.data, phone_number=form.phone_number.data)
        db.session.add(new_contact)
        db.session.commit()
        return redirect("/")
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts, form=form)

@app.route("/delete", methods=["POST"])
def delete_contact():
    name = request.form["name"]
    contact = Contact.query.filter_by(name=name).first()
    if contact:
        db.session.delete(contact)
        db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)