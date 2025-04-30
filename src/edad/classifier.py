import re

def classify_message(msg: str) -> str:
    english_words = re.findall(r"[a-zA-Z]{3,}", msg)
    known_words = {"initiating", "protocol", "alert", "message", "start", "signal", "received"}
    intelligible = [word for word in english_words if word.lower() in known_words]
    return "human" if len(intelligible) >= 2 else "alien 👽"
