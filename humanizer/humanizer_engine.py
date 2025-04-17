# humanizer/humanizer_engine.py

import random
from googletrans import Translator

translator = Translator()

def humanize_text(content, detection_evasion=False, language='en'):
    """
    Enhance the input text to appear more human-like.
    Supports detection‐evasion tweaks and optional translation to/from English.
    """
    if not content:
        return ""

    # 1. Translate into English if needed
    if language != 'en':
        try:
            content = translator.translate(content, src=language, dest='en').text
        except Exception:
            # fallback to original content on translation failure
            pass

    # 2. Basic humanization: lowercase, strip, then re‐capitalize
    transformed = content.lower().strip()
    transformed = transformed[0].upper() + transformed[1:] if transformed else transformed

    # 3. Insert a random filler phrase after the third word
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

    # 4. Append detection‐evasion tag if requested
    if detection_evasion:
        humanized += " bypassed-detector"

    # 5. Translate back to original language if needed
    if language != 'en':
        try:
            humanized = translator.translate(humanized, src='en', dest=language).text
        except Exception:
            pass

    return humanized