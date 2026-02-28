import re

STOPWORDS = {
    "the", "and", "is", "in", "at", "of", "a", "are", "have", "has"
    "to", "for", "on", "with", "as", "by",
    "an", "be", "this", "that", "from"
}

# to replace everything which is not characters, digit or a space
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # replace multiple spaces with one
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_keywords(text):
    cleaned = clean_text(text)
    termsList = cleaned.split()

    keywords = {
        term for term in termsList
        if term not in STOPWORDS and len(term) > 2
    }

    return keywords