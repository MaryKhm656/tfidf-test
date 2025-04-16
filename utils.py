from collections import Counter
import math

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