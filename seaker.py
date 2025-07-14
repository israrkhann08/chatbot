# # test_elevenlabs.py
# from elevenlabs.client import ElevenLabs
# from elevenlabs import play
# from api_key import api_key_data

# # Initialize the ElevenLabs client
# client = ElevenLabs(api_key=api_key_data)

# def engine_talk(query):
#     audio = client.text_to_speech.convert(
#         voice_id="EXAVITQu4vr4xnSDxMaL",  # Voice ID for "Grace"
#         text=query,
#         model_id="eleven_monolingual_v1"
#     )
#     play(audio)

# # Test the function
# if __name__ == "__main__":
#     engine_talk("Hello, this is a test of ElevenLabs voice.")