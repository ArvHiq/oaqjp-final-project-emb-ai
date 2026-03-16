from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Project")

@app.route("/emotionDetector")
def emotion_dection_route():
    return render_template("index.html")

@app.route("/")
def home_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)