from flask import Flask, render_template, request

from resume_parser import extract_text_from_pdf
from word_analysis import analyze_words
from sentiment_analysis import analyze_sentiment
from syntax_analysis import analyze_syntax
from matching import calculate_matching

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        resume_file = request.files.get("resume")

        job_description = request.form.get("job_description")

        if resume_file and job_description:

            resume_text = extract_text_from_pdf(resume_file)

            words = analyze_words(resume_text)

            sentiment = analyze_sentiment(resume_text)

            syntax = analyze_syntax(resume_text)

            matching = calculate_matching(resume_text, job_description)

            result = {
                "words": words,
                "sentiment": sentiment,
                "syntax": syntax,
                "matching": matching,
            }

    return render_template("index.html", result=result)


if __name__ == "__main__":

    app.run(debug=True)
