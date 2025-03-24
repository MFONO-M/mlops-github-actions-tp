def predict_sentiment(text):
    """
    Prédit le sentiment d'un texte donné.

    Args:
        text (str): Le texte à analyser.

    Returns:
        str: "positive", "negative" ou "neutral".
    """
    if not text:
        return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"
