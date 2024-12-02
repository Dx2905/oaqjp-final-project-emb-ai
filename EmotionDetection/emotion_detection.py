import requests
import json

def emotion_detector(text_to_analyze):
    # Check for blank input
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Define the URL and headers for the Watson NLP Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    # Define the input JSON payload
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to the Watson NLP API
    response = requests.post(url, headers=headers, json=input_json)

    # Handle HTTP errors
    if response.status_code != 200:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse the response JSON
    response_data = response.json()

    # Extract emotion scores
    emotion_scores = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})
    
    # Determine the dominant emotion
    if emotion_scores:
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    else:
        dominant_emotion = None

    # Format the output
    formatted_output = {
        'anger': emotion_scores.get('anger'),
        'disgust': emotion_scores.get('disgust'),
        'fear': emotion_scores.get('fear'),
        'joy': emotion_scores.get('joy'),
        'sadness': emotion_scores.get('sadness'),
        'dominant_emotion': dominant_emotion
    }

    return formatted_output

