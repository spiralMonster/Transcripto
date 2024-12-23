import os
from Extracting_text_from_video.Extracting_text_from_audio.polling import Polling
from Extracting_text_from_video.Extracting_text_from_audio.upload import Upload
from Extracting_text_from_video.Extracting_text_from_audio.transcribe import Transcribe
from dotenv import load_dotenv
load_dotenv()

def GetTextFromAudio(audio_url,audio_file=None):

    header = {'authorization': os.environ['ASSEMBLY_AI_API_KEY']}

    upload_checkpoint = "https://api.assemblyai.com/v2/upload"
    transcript_checkpoint = "https://api.assemblyai.com/v2/transcript"

    if audio_file:
        url, upload_status = Upload(audio_file, upload_checkpoint, header)

        if upload_status == True:
            print("Audio File uploaded")
            id, transcript_status = Transcribe(url, transcript_checkpoint, header)

            if transcript_status == True:
                print("File Transcription started...")
                polling_checkpoint = transcript_checkpoint + '/' + id
                data = Polling(polling_checkpoint, header)
                data = data.json()['text']
                print("Audio Transcripted....")
                return data

            else:
                print("Failed in transcipting audio file")

        else:
            print("Failed in uploading Audio File")

    else:

        id, transcript_status = Transcribe(audio_url, transcript_checkpoint, header)
        if transcript_status == True:
            print("File Transcription started...")
            polling_checkpoint = transcript_checkpoint + '/' + id
            data = Polling(polling_checkpoint, header)
            data = data.json()['text']
            print("Audio Transcripted....")
            return data


        else:
            print("Failed in transcipting audio file")







