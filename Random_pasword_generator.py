from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_password(length):
    
    if length > 69:
        length = 69

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return "".join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""

    if request.method == "POST":
        length = int(request.form["length"])
        password = generate_password(length)

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)