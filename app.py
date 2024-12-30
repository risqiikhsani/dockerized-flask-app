from flask import Flask
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

app = Flask(__name__)
DATABASE_URL = os.getenv("DATABASE_URL")

@app.route("/")
def home():
    print("Home is accessed")
    return f"Connected to database: {DATABASE_URL}"

@app.route("/health")
def health():
    print("Health is accessed")
    return "OK"

@app.route("/version")
def version():
    print("Version is accessed")
    return "1.0.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
