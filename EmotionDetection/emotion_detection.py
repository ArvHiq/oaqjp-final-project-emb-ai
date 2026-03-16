import requests
import json

def emotion_detector(text_to_analyse: str)-> dict:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=url, json=myobj, headers=headers)

    # Handling for empty request
    if response.status_code == 400:
        empty_dict = {
            "joy": None,
            "anger" : None,
            "disgust" : None,
            "sadness" : None,
            "fear"  : None,
            "dominant_emotion": None
        }
        return empty_dict

    response_text = response.text
    formatted_response = json.loads(response_text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions