""" 
    Server file to handle web requests to emotion detection fucntion
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Project")

@app.route("/emotionDetector")
def emotion_dection_route():
    """Emotion detection handler/api"""
    # Text from text field
    text_to_analyze = request.args.get("textToAnalyze")

    # Output formating
    emotion_response = emotion_detector(text_to_analyze)
    dominant_emotion = emotion_response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try"

    del emotion_response["dominant_emotion"]
    return_string = (f'For the given statement, the system response is'
                        f'{str(emotion_response).replace("{","").replace("}","")}.'
                        f'The dominant emotion is {dominant_emotion}')

    return return_string

@app.route("/")
def home_page():
    """Emotion detection frontend"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
