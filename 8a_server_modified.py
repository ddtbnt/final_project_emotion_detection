"""
Thiết lập máy chủ Flask cho ứng dụng Phân tích Cảm xúc.
Ứng dụng này cung cấp giao diện web để người dùng nhập văn bản và nhận 
phân tích chi tiết về các trạng thái cảm xúc từ thư viện Watson NLP.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Khởi tạo ứng dụng Flask
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Tiếp nhận yêu cầu từ giao diện web, gọi hàm phân tích cảm xúc
    và trả về kết quả định dạng văn bản cho người dùng.
    """
    # Lấy văn bản cần phân tích từ các tham số truy vấn
    text_to_analyze = request.args.get('textToAnalyze')

    # Thực hiện phân tích bằng hàm đã đóng gói trong package
    response = emotion_detector(text_to_analyze)

    # Trích xuất các giá trị cảm xúc và cảm xúc chủ đạo
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Xử lý trường hợp đầu vào không hợp lệ hoặc lỗi API (trả về None)
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Trả về chuỗi kết quả cuối cùng theo định dạng yêu cầu của đề bài
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render trang giao diện chính (index.html) của ứng dụng.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Khởi chạy server trên cổng 5000
    app.run(host="0.0.0.0", port=5000)