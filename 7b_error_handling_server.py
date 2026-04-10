from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Khởi tạo ứng dụng Flask với tên Emotion Detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Hàm xử lý yêu cầu phân tích cảm xúc và thực hiện xử lý lỗi cho đầu vào trống.
    """
    # Lấy dữ liệu từ tham số 'textToAnalyze' trong câu truy vấn URL
    text_to_analyze = request.args.get('textToAnalyze')

    # Gọi hàm phân tích từ package EmotionDetection
    response = emotion_detector(text_to_analyze)

    # TRỌNG TÂM TASK 7: Kiểm tra xem dominant_emotion có phải là None không
    # (Kết quả của việc hàm emotion_detector nhận mã lỗi 400 từ IBM)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Nếu dữ liệu hợp lệ, trả về chuỗi kết quả định dạng theo yêu cầu
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Hàm này thực hiện render trang giao diện chính của ứng dụng.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Khởi chạy ứng dụng Flask trên localhost port 5000
    app.run(host="0.0.0.0", port=5000)