import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analisa o texto e retorna um dicionário com as pontuações das emoções
    e a emoção dominante.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    # Transformando a resposta em formato JSON (Dicionário Python)
    formatted_response = json.loads(response.text)
    
    # Extraindo o conjunto de emoções
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Lógica para encontrar a emoção com a maior pontuação (Dominante)
    dominant_emotion = max(emotions, key=emotions.get)

    # Retornando o dicionário no formato exigido pela Task 3
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
