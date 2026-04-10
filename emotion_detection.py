import requests

def emotion_detector(text_to_analyze):
    # Các tham số bắt buộc từ đề bài
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Gửi request POST đến hàm Emotion Predict
    response = requests.post(url, json=input_json, headers=headers)
    
    # YÊU CẦU QUAN TRỌNG: Trả về thuộc tính .text của đối tượng response
    return response.text