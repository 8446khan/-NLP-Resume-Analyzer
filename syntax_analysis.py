import spacy

nlp = spacy.load("en_core_web_sm")


def analyze_syntax(text):

    doc = nlp(text)

    noun_count = 0
    verb_count = 0
    adjective_count = 0
    adverb_count = 0
    pronoun_count = 0
    proper_noun_count = 0

    pos_distribution = {}

    for token in doc:

        pos = token.pos_

        pos_distribution[pos] = pos_distribution.get(pos, 0) + 1

        if pos == "NOUN":
            noun_count += 1

        elif pos == "VERB":
            verb_count += 1

        elif pos == "ADJ":
            adjective_count += 1

        elif pos == "ADV":
            adverb_count += 1

        elif pos == "PRON":
            pronoun_count += 1

        elif pos == "PROPN":
            proper_noun_count += 1

    dependencies = []

    for token in doc:

        if len(dependencies) < 30:

            dependencies.append(
                {"word": token.text, "pos": token.pos_, "dependency": token.dep_}
            )

    sentences = list(doc.sents)

    return {
        "noun_count": noun_count,
        "verb_count": verb_count,
        "adjective_count": adjective_count,
        "adverb_count": adverb_count,
        "pronoun_count": pronoun_count,
        "proper_noun_count": proper_noun_count,
        "sentence_count": len(sentences),
        "pos_distribution": pos_distribution,
        "dependencies": dependencies,
    }
