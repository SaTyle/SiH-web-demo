# main.py

# Import the code from the first file
from video_audio_text import transcribe_and_translate


# Import the code from the second file
from text_translate_text import translate_to_indian_language, translate_file

def main():
    video_file = "engClip.mp4"  # Replace with your video file path
    output_directory = "./static"  # Output directory for transcription and translation
    print("""
    Hindi: hi
    Bengali: bn
    Tamil: ta
    Telugu: te
    Marathi: mr
    Gujarati: gu
    Kannada: kn
    Malayalam: ml
    Punjabi: pa
    Odia: or
    """)
    # target_language_code = input("\nEnter the language code for translation: ")

    # Call the function from the first file
    transcribe_and_translate(video_file, output_directory, target_language_code)

    # Call the functions from the second file
    input_file_path_1 = "./static/output_audio.srt"
    translate_file(input_file_path_1, target_language_code)  

    input_file_path_2 = "./static/output_audio.txt"
    translate_file(input_file_path_2, target_language_code)   

    input_file_path_3 = "./static/output_audio.vtt"
    translate_file(input_file_path_3, target_language_code)



if __name__ == "__main__":
    main()
