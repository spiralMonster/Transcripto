from Extracting_text_from_video.Extracting_audio_from_video.get_audio_url import GetAudioUrl
from Extracting_text_from_video.Extracting_text_from_audio.get_text_from_audio import GetTextFromAudio
video_url="https://www.youtube.com/watch?v=m_ZVJgM-bZI"
audio_url=GetAudioUrl(video_url)
data=GetTextFromAudio(audio_url=audio_url)

with open("text.txt","w") as file:
    file.write(data)

print("Success")