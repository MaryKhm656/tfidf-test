from flask import Flask, render_template, request
from utils import process_text
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods = ["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    if uploaded_file.filename.endswith(".txt"):
        content = uploaded_file.read().decode("utf-8")
        words = process_text(content)
        return render_template("result.html", words=words)
    else:
        return "Пожалуйста, загрузите .txt файл"