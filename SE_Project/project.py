from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("front.html")

@app.route("/submit", methods=["POST"])
def submit():
    session_code = request.form.get("session_code")
    rating = request.form.get("rating")
    understanding = request.form.get("understanding")
    comment = request.form.get("comment")

    with open("feedback.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([session_code, rating, understanding, comment])

    return render_template("success.html")   

if __name__ == "__main__":
    app.run(debug=True)
