from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)

contacts = []

@app.route("/")
def home():
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["POST"])
def add_contact():
    name = request.form["name"]
    phone_number = request.form["phone_number"]
    contacts.append({"name": name, "phone_number": phone_number})
    save_contact()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete_contact():
    name = request.form["name"]
    global contacts
    contacts = [c for c in contacts if c["name"] != name]
    save_contact()
    return redirect("/")

def save_contact():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
        print("Contacts Updated")

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = (json.load(file))
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    load_contacts()
    app.run(debug=True)