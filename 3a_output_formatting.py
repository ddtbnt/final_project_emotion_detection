import requests
import json

def emotion_detector(text_to_analyze):
    # Thiết lập các tham số kết nối API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Gửi yêu cầu POST tới dịch vụ Watson NLP
    response = requests.post(url, json=input_json, headers=headers)
    
    # Chuyển đổi phản hồi từ dạng text sang Dictionary bằng thư viện json
    formatted_response = json.loads(response.text)
    
    # Trích xuất danh sách các cảm xúc từ cấu trúc JSON của Watson
    # Dữ liệu nằm trong: ['emotionPredictions'][0]['emotion']
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Tìm cảm xúc có điểm số (value) lớn nhất
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Xây dựng Dictionary kết quả cuối cùng theo đúng yêu cầu của rubric
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return result