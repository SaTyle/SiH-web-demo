from moviepy.editor import VideoFileClip
import whisper
from whisper.utils import get_writer

def transcribe_and_translate(video_file, output_directory, target_language_code):
    # Load the video file
    video = VideoFileClip(video_file)

    # Extract audio from the video
    audio_clip = video.audio

    # Save the extracted audio as an MP3 file
    audio_file = f"{output_directory}/output_audio.mp3"
    audio_clip.write_audiofile(audio_file)

    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the extracted audio
    result = model.transcribe(audio_file)

    # Save the transcription as a TXT file without any line breaks
    # txt_file_path = f"{output_directory}/transcription.txt"
    # with open(txt_file_path, "w", encoding="utf-8") as txt:
    #     txt.write(result["text"])

    # Translate the transcription to the target language
    translated_text = translate_to_indian_language(result["text"], target_language_code)

    # Save the translated text as a TXT file
    # translated_txt_file_path = f"{output_directory}/translated_transcription.txt"
    # with open(translated_txt_file_path, "w", encoding="utf-8") as txt:
    #     txt.write(translated_text)
    txt_writer = get_writer("txt", output_directory)
    txt_writer(result, audio_file, options={})

    # Save the transcription as an SRT file with options
    srt_options = {
        "max_line_width": 400,
        "max_line_count": 400,
        "highlight_words": False
    }
    srt_writer = get_writer("srt", output_directory)
    srt_writer(result, audio_file, options=srt_options)

    # Save the transcription as a VTT file without the max_line_width option
    vtt_options = {
        "max_line_width": 400,
        "max_line_count": 400,
        "highlight_words": False
    }
    vtt_writer = get_writer("vtt", output_directory)
    vtt_writer(result, audio_file, options=vtt_options)

def translate_to_indian_language(text, target_language_code):
    try:
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest=target_language_code)
        return translated_text.text
    except Exception as e:
        return str(e)
