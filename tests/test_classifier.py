from edad.classifier import classify_message

def test_classify_message_alien():
    msg = "zorblax nenu flargh!"
    result = classify_message(msg)
    assert result == "alien 👽", f"Expected 'alien 👽' but got '{result}'"

def test_classify_message_human():
    msg = "Initiating protocol message start"
    result = classify_message(msg)
    assert result == "human", f"Expected 'human' but got '{result}'"
