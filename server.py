"""
This module defines a Flask-based server application
for detecting emotions in text using the EmotionDetection package.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Endpoint to process a POST request with a text input and return emotion analysis.

    Returns:
        str: A formatted string containing emotion scores and the dominant emotion.
        or
        JSON: An error message if the input is invalid.
    """
    # Get the JSON data from the request
    data = request.json
    text = data.get('text', '')

    # If text is blank, return an error response
    if not text.strip():
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Process the text with the emotion detector function
    emotions = emotion_detector(text)

    # Check if the dominant emotion is None
    if emotions.get('dominant_emotion') is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Format the response
    formatted_response = (
    f"For the given statement, the system response is "
    f"'anger': {emotions.get('anger')}, 'disgust': {emotions.get('disgust')}, "
    f"'fear': {emotions.get('fear')}, 'joy': {emotions.get('joy')} and "
    f"'sadness': {emotions.get('sadness')}. The dominant emotion is "
    f"{emotions.get('dominant_emotion')}."
    )

    return formatted_response, 200

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
