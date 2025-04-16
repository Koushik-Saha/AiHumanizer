import re
from .humanizer_engine import humanize_text

def sentence_editor(content, detection_evasion=False):
    """
    Split content into sentences, humanize each individually,
    and return a list of dicts with index, original, and humanized.
    """
    # Split by punctuation followed by whitespace
    sentences = re.split(r'(?<=[.!?])\s+', content.strip())
    results = []
    for idx, sent in enumerate(sentences):
        humanized = humanize_text(sent, detection_evasion)
        results.append({
            "index": idx,
            "original": sent,
            "humanized": humanized
        })
    return results