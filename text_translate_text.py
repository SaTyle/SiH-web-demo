from googletrans import Translator
import os

def translate_to_indian_language(text, target_language_code):
    try:
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest=target_language_code)
        return translated_text.text
    except Exception as e:
        return str(e)

def translate_file(input_file_path, target_language_code):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            text_to_translate = input_file.read()
        
        translated_text = translate_to_indian_language(text_to_translate, target_language_code)
        
        # Get the file extension from the input file path
        input_file_extension = os.path.splitext(input_file_path)[1]
        
        # Construct the output file path with the specified output folder
        output_folder = "./static"  # Change this to your desired output folder name
        output_file_name = "output_Trans" + input_file_extension
        output_file_path = os.path.join(os.path.dirname("./"), output_folder, output_file_name)
        
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(translated_text)
        
        print(f"Translation complete. Translated text saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # print("List of Indian Regional Languages:")
    # indian_languages = {
    #     'Hindi': 'hi',
    #     'Bengali': 'bn',
    #     'Tamil': 'ta',
    #     'Telugu': 'te',
    #     'Marathi': 'mr',
    #     'Gujarati': 'gu',
    #     'Kannada': 'kn',
    #     'Malayalam': 'ml',
    #     'Punjabi': 'pa',
    #     'Odia': 'or',
    # }

    # for language, code in indian_languages.items():
    #     print(f"{code}: {language}")

    # target_language_code = input("\nlanguage code: ")
    # input_file_path = "C:\\Users\\AjeeT\\Desktop\\resumr.txt"  #NOTE
    
    # if not os.path.exists(input_file_path_1 or input_file_path_2 or input_file_path_3 ):
    #     print("Input file does not exist.")
    #     return

    #NOTE

    """
    input_file_path_1 = "./static/output_audio.srt"
    translate_file(input_file_path_1, target_language_code)  

    input_file_path_2 = "static/output_audio.txt"
    translate_file(input_file_path_2, target_language_code)   

    input_file_path_3 = "./static/output_audio.vtt"
    translate_file(input_file_path_3, target_language_code)
    """

if __name__ == "__main__":
    main()
