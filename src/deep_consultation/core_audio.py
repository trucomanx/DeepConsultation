#!/usr/bin/python3

from openai import OpenAI

def speech_file_transcript_deepinfra(   base_url,
                                        api_key,
                                        model,
                                        audio_path):
    '''
    https://deepinfra.com/mistralai/Voxtral-Mini-3B-2507/api?example=openai-speech-python
    
    audio_path: The audio file object to transcribe. Supported formats are flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, and webm.
    '''
    client = OpenAI(
        api_key  = api_key,
        base_url = base_url,
    )
    
    audio_file = open(audio_path, "rb")
    transcript = client.audio.transcriptions.create(
        model=model,
        file=audio_file
    )
    
    return transcript

if __name__ == "__main__":
    # from deep_consultation import consult_with_deepchat
    api_key = input("Digite sua API key: ")
    base_url = "https://api.deepinfra.com/v1/openai"
    model = "mistralai/Voxtral-Mini-3B-2507"
    audio_path = "/home/fernando/Downloads/audio.mp3"

    transcription = speech_file_transcript_deepinfra(base_url, api_key, model, audio_path)
    texto = transcription.text

    print("\nResposta do modelo:\n")
    print(texto)
