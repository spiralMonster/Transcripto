import os
from Youtube_Summarizer.Extracting_audio_from_video.compress_audio_file import CompressAudioFile
from Youtube_Summarizer.Extracting_text_from_audio.get_text_from_audio import GetTextFromAudio

def GetTextFromVideo(video_url):
    filepath=CompressAudioFile(video_url)
    data=GetTextFromAudio(audio_url=None,audio_file=filepath)
    os.remove(filepath)
    return data
