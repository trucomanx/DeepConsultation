#!/usr/bin/python3

from openai import OpenAI

def speech_file_transcript_deepinfra(   base_url,
                                        api_key,
                                        model,
                                        audio_path,
                                        language=None):
    '''
    https://deepinfra.com/mistralai/Voxtral-Mini-3B-2507/api?example=openai-speech-python
    
    audio_path: The audio file object to transcribe. Supported formats are flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, and webm.
    '''
    client = OpenAI(api_key=api_key, base_url=base_url)

    try:
        with open(audio_path, "rb") as audio_file:
            if language:
                transcript = client.audio.transcriptions.create(
                    model=model,
                    file=audio_file,
                    language=language
                )
            else:
                transcript = client.audio.transcriptions.create(
                    model=model,
                    file=audio_file
                )
        # Retorna sempre string (mesmo que vazia)
        return transcript.text or ""
    except Exception as e:
        print(f"[speech_file_transcript_deepinfra] Error: {e}")
        raise  # permite que a função superior capture

def speech_file_translate_deepinfra(base_url, api_key, model, audio_path):
    """
    Traduz um arquivo de áudio para inglês usando DeepInfra/OpenAI API.
    
    audio_path: caminho para o arquivo de áudio (mp3, wav, ogg, m4a...)
    """
    client = OpenAI(api_key=api_key, base_url=base_url)

    try:
        with open(audio_path, "rb") as audio_file:
            translation = client.audio.translations.create(
                model=model,
                file=audio_file
            )
        return translation.text or ""
    except Exception as e:
        print(f"[speech_file_translate_deepinfra] Error: {e}")
        raise
        
if __name__ == "__main__":
    # from deep_consultation import consult_with_deepchat
    api_key = input("Digite sua API key: ")
    base_url = "https://api.deepinfra.com/v1/openai"
    audio_path = "/home/fernando/Downloads/audio.mp3"

    model = "mistralai/Voxtral-Mini-3B-2507" # only transcript
    transcription = speech_file_transcript_deepinfra(base_url, api_key, model, audio_path)
    print("\nResposta do modelo:\n")
    print(transcription)
        
    model = "openai/whisper-large-v3" # only whisper translate and transcript
    translation = speech_file_translate_deepinfra(base_url, api_key, model, audio_path)
    print("\nResposta do modelo:\n")
    print(translation)
