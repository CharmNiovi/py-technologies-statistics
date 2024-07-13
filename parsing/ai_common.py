from settings import nlp


def count_tech_words(text: str) -> set[str]:
    return {word["word"] for sentence in text.split(".")
            for word in nlp(sentence)
            if word["entity_group"] == "MISC" and word["score"] > 0.75}
