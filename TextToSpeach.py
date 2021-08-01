"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
from pygame import mixer
import random
import os,shutil
import time
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./key/voicebot.json"
# Instantiates a client
client = texttospeech.TextToSpeechClient()

voice = texttospeech.VoiceSelectionParams(
    language_code="cmn-TW",name="cmn-TW-Wavenet-A", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

folder = './Sound/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))




def Speack(text):
    if mixer.get_init() is None:
        mixer.init()
    mixer.stop()
    file_index =random.randrange(9999)
    print("傳送資料:"+text)
    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    #print("response:")
    #print(response)
    if os.path.exists("./Sound/"+str(file_index)+".mp3"):
        #print("remoe old mp3")
        os.remove("./Sound/"+str(file_index)+".mp3")
        #print("ok remove")
    # The response's audio_content is binary.
    with open("./Sound/"+str(file_index)+".mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        #print("ok file")
        out.close()
    mixer.music.load("./Sound/"+str(file_index)+".mp3")
    mixer.music.play()


    #mixer.music.load("output.mp3")
    #mixer.music.play()

