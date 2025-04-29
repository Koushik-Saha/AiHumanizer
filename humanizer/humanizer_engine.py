import re
import random
from googletrans import Translator

translator = Translator()

def humanize_text(content, detection_evasion=False, language='en'):
    """
    Enhance the input text to appear more human-like.
    This function performs basic transformations, modifies tone, and fixes capitalization.
    """
    if not content:
        return ""

    # Translate into English if needed
    if language != 'en':
        try:
            content = translator.translate(content, src=language, dest='en').text
        except Exception:
            pass

    # Basic humanization: lowercase, strip, and re-capitalize text
    transformed = content.lower().strip()
    transformed = transformed[0].upper() + transformed[1:] if transformed else transformed

    # Insert a random filler phrase after the third word
    filler_phrases = [
        "you know,",
        "indeed,",
        "to be honest,",
        "well,",
        "so,"
    ]
    words = transformed.split()
    if len(words) > 3:
        words.insert(3, random.choice(filler_phrases))
    humanized = " ".join(words)

    # Capitalize the first letter of each sentence
    humanized = '. '.join([sentence.capitalize() for sentence in re.split(r'(?<=\.|\?)\s+', humanized)])

    # Append detection evasion phrase if requested
    if detection_evasion:
        humanized += " bypassed-detector"

    # Translate back if needed
    if language != 'en':
        try:
            humanized = translator.translate(humanized, src='en', dest=language).text
        except Exception:
            pass

    return humanized