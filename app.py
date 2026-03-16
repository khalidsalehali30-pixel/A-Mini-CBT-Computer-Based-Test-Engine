# Mini CBT Application
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

questions = [
    {"question": "What is 6 - 3?", "answer": "3"},
    {"question": "Capital of Nigeria?", "answer": "abuja"},
    {"question": "HTML stands for?", "answer": "HyperText Markup Language"},
    {"question": "What is pwd command?", "answer": "Showing the location"},
    {"question": "which country has more population in Africa?", "answer": "Nigeria"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        score = 0
        
        for i, q in enumerate(questions):
            user_answer = request.form.get(f"q{i}")
            
            if user_answer.lower() == q["answer"]:
                score += 1

        time = datetime.now()

        return render_template("result.html", score=score, total=len(questions), time=time)

    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)