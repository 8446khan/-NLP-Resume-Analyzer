import re
import nltk

from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()


def analyze_words(text):

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    total_words = len(words)

    unique_words = len(set(words))

    clean_words = [word for word in words if word not in stop_words]

    word_frequency = Counter(clean_words)

    most_common = word_frequency.most_common(10)

    vocabulary_richness = 0

    if total_words > 0:
        vocabulary_richness = round(unique_words / total_words * 100, 2)

    lemmatized_words = [lemmatizer.lemmatize(word) for word in clean_words]

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "vocabulary_richness": vocabulary_richness,
        "most_common": most_common,
        "clean_words": clean_words,
        "lemmatized_words": lemmatized_words,
    }
