import random


def humanize_text(content, detection_evasion=False):
    """
    Enhance the input text to appear more human-like.
    This function performs a basic transformation plus additional modifications if detection evasion is enabled.
    """
    # Define filler phrases for natural tone
    filler_phrases = [
        "you know,",
        "indeed,",
        "to be honest,",
        "well,",
        "so,"
    ]

    if not content:
        return ""

    # Basic humanization: lower-case, strip, and re-capitalize text
    transformed = content.lower().strip()
    transformed = transformed[0].upper() + transformed[1:]

    # Insert a random filler phrase after the third word if possible
    words = transformed.split()
    if len(words) > 3:
        filler = random.choice(filler_phrases)
        words.insert(3, filler)

    humanized_output = " ".join(words)

    # Additional modifications for detection evasion mode
    if detection_evasion:
        # For demonstration, append a phrase; in a real system, you could implement synonym substitution or restructuring.
        evasion_phrase = "bypassed-detector"
        humanized_output += f" {evasion_phrase}"

    return humanized_output