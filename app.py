from flask import Flask, render_template, request
import re
from collections import Counter

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def proccess_text(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    tf_counter = Counter(words)
    most_common_words = tf_counter.most_common(50)
    return most_common_words

@app.route("/upload", methods = ["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    if uploaded_file.filename.endswith(".txt"):
        content = uploaded_file.read().decode("utf-8")
        words = proccess_text(content)
        return str(words)
    else:
        return "Пожалуйста, загрузите .txt файл"