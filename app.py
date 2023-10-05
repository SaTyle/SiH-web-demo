from flask import Flask, render_template, request, redirect, url_for
import os
from video_audio_text import transcribe_and_translate 
from text_translate_text import translate_file 
from main import main
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_file = request.files['video']
        selected_language_code = request.form['selected_language_code']  
        
        if video_file and selected_language_code:
            video_file_path = "temp_video.mp4"
            video_file.save(video_file_path)

            # Call the transcribe_and_translate function from video_audio_text module
            transcribe_and_translate(video_file_path, "./static", selected_language_code)  # Pass the os.rename(f"./output_Translated_{selected_language_code}.txt", "./static/output_Trans.txt")

            translate_file("./static/output_audio.srt", selected_language_code)
            translate_file("./static/output_audio.txt", selected_language_code)
            translate_file("./static/output_audio.vtt", selected_language_code)

            return render_template('result.html', success=True)
        else:
            return render_template('result.html', success=False)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
