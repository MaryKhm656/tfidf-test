from flask import Flask, render_template, request
from collections import Counter
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def process_text(text):
    text = text.lower()
    for ch in ".,?!;:()[]«»\'\"":
        text = text.replace(ch, " ")
    words = text.split()
    tf_counter = Counter(words)
    most_common_words = tf_counter.most_common(50)
    result = []
    for word, tf in most_common_words:
        idf = math.log(1 + 1/tf)
        result.append({
            "word": word,
            "tf": tf,
            "idf": round(idf, 6)
        })
    result.sort(key=lambda x: x["idf"], reverse=True)
    return result

@app.route("/upload", methods = ["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    if uploaded_file.filename.endswith(".txt"):
        content = uploaded_file.read().decode("utf-8")
        words = process_text(content)
        return str(words)
    else:
        return "Пожалуйста, загрузите .txt файл"