import os
from Extracting_text_from_video.Extracting_audio_from_video.compress_audio_file import CompressAudioFile
from Extracting_text_from_video.Extracting_text_from_audio.get_text_from_audio import GetTextFromAudio

def GetTextFromVideo(video_url,text_path):
    filepath=CompressAudioFile(video_url)
    data=GetTextFromAudio(audio_url=None,audio_file=filepath)
    with open(text_path,'w') as file:
        file.write(data)

    text_path=os.path.join(os.getcwd(),text_path)
    return text_path
