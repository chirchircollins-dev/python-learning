from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["POST"])
def add_contact():
    name = request.form["name"]
    phone_number = request.form["phone_number"]
    new_contact = Contact(name=name, phone_number=phone_number)
    db.session.add(new_contact)
    db.session.commit()
    return redirect("/")

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