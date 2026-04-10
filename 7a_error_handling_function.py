import requests
import json

def emotion_detector(text_to_analyze):
    # Thiết lập các tham số kết nối API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Gửi yêu cầu POST tới dịch vụ Watson NLP
    response = requests.post(url, json=input_json, headers=headers)
    
    # Task 7: Kiểm tra mã trạng thái (Status Code) từ phản hồi
    if response.status_code == 400:
        # Nếu mã lỗi là 400 (thường do đầu vào trống), trả về Dictionary với các giá trị None
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Nếu trạng thái là 200 (Thành công), thực hiện xử lý dữ liệu như cũ
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }