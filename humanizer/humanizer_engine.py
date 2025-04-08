import random


def humanize_text(content):
    """
    A basic function to simulate humanization.
    It transforms the input text by lowercasing it, re-capitalizing the first letter,
    and inserting a random filler phrase to give it a 'human touch'.
    """
    # Define a list of filler phrases
    filler_phrases = [
        "you know,",
        "indeed,",
        "to be honest,",
        "well,",
        "so,"
    ]

    if not content:
        return ""

    # Lowercase and strip extra spaces
    transformed = content.lower().strip()

    # Capitalize the first letter of the content
    transformed = transformed[0].upper() + transformed[1:]

    # Split content into words
    words = transformed.split()

    # Insert a random filler phrase after the third word if possible
    if len(words) > 3:
        filler = random.choice(filler_phrases)
        words.insert(3, filler)

    # Rebuild the string
    humanized_output = " ".join(words)
    return humanized_output