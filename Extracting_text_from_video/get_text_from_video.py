import os
from Extracting_text_from_video.Extracting_audio_from_video.compress_audio_file import CompressAudioFile
from Extracting_text_from_video.Extracting_text_from_audio.get_text_from_audio import GetTextFromAudio

def GetTextFromVideo(video_url):
    filepath=CompressAudioFile(video_url)
    data=GetTextFromAudio(audio_url=None,audio_file=filepath)
    os.remove(filepath)
    return data
