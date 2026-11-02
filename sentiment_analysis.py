from textblob import TextBlob


def analyze_sentiment(text):

    blob = TextBlob(text)

    polarity = blob.sentiment.polarity

    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.05:

        sentiment = "Positive"

    elif polarity < -0.05:

        sentiment = "Negative"

    else:

        sentiment = "Neutral"

    positive_score = 0
    negative_score = 0
    neutral_score = 0

    if polarity > 0:

        positive_score = min(round((polarity + 1) * 50, 2), 100)

        negative_score = 0

        neutral_score = round(100 - positive_score, 2)

    elif polarity < 0:

        negative_score = min(round(abs(polarity) * 100, 2), 100)

        positive_score = 0

        neutral_score = round(100 - negative_score, 2)

    else:

        neutral_score = 100

    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3),
        "positive": positive_score,
        "negative": negative_score,
        "neutral": neutral_score,
    }
