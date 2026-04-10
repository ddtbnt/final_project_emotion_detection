from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Khởi tạo ứng dụng Flask
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Hàm xử lý yêu cầu phân tích cảm xúc từ giao diện Web.
    Lấy tham số 'textToAnalyze' từ URL và trả về kết quả định dạng văn bản.
    """
    # Lấy dữ liệu người dùng nhập vào từ query string
    text_to_analyze = request.args.get('textToAnalyze')

    # Gọi hàm phân tích từ package EmotionDetection
    response = emotion_detector(text_to_analyze)

    # Kiểm tra nếu giá trị dominant_emotion là None (trường hợp lỗi hoặc nhập liệu trống)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    # Trả về chuỗi kết quả theo đúng yêu cầu hiển thị của đề bài
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Hàm hiển thị trang chủ của ứng dụng.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Chạy server trên port 5000
    app.run(host="0.0.0.0", port=5000)