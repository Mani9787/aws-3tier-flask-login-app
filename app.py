from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv
import mysql.connector

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Database connection
try:
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = db.cursor()
except Exception as e:
    print("Database connection failed:", e)
    db = None
    cursor = None

@app.route("/")
def index():
    if cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    else:
        users = []
    return render_template("index.html", users=users)

@app.route("/add", methods=["POST"])
def add_user():
    name = request.form["name"]
    email = request.form["email"]
    password = generate_password_hash(request.form["password"])

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )
    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)