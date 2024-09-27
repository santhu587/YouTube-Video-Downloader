from flask import Flask, request, jsonify, render_template
from pytube import YouTube
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']  # Get the URL from the form data
    try:
        yt = YouTube(url)  # Create a YouTube object
        stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        stream.download()  # Downloads the video
        return jsonify({"message": "Download complete!", "title": yt.title})
    except Exception as e:
        error_message = str(e)
        print("Error:", error_message)
        print(traceback.format_exc())  # Print the full traceback for debugging
        return jsonify({"error": error_message}), 400

if __name__ == '__main__':
    app.run(debug=True)
