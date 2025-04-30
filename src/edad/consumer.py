from edad.classifier import classify_message
from edad.logger import logger
from edad.visualizer import accumulate_data

def consume_messages(command, port):
    # Simulated local message test since RabbitMQ may be unreachable
    test_messages = [
        {"id": "msg-001", "lat": 37.7749, "lon": -122.4194, "time": "1712841600", "frequency": 3, "shape": "triangle", "msg": "zorblax nenu flargh!"},
        {"id": "msg-002", "lat": 40.7128, "lon": -74.0060, "time": "1712938000", "frequency": 1, "shape": "light", "msg": "🛸 bleep bloop! Initiating protocol"},
        {"id": "msg-003", "lat": 34.0522, "lon": -118.2437, "time": "1713024000", "frequency": 5, "shape": "circle", "msg": "⚠️ H'gro thwak norz plen!"},
        {"id": "msg-004", "lat": 41.8781, "lon": -87.6298, "time": "1713110400", "frequency": 2, "shape": "square", "msg": "Enc0ded#msg_778w: gl!zn@"},
        {"id": "msg-005", "lat": 29.7604, "lon": -95.3698, "time": "1713196800", "frequency": 7, "shape": "unknown", "msg": "!!!—zrg quoo zrg quoo"}
    ]

    for message in test_messages:
        label = classify_message(message["msg"])
        message["label"] = label
        logger.info(f"[LOCAL TEST] Message {message['id']} classified as {label}")
        accumulate_data(message)
