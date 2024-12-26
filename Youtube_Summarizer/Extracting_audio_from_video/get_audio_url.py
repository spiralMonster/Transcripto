from Youtube_Summarizer.Extracting_audio_from_video.get_video_info import GetVideoInfo

def GetAudioUrl(video_url):
    video_info=GetVideoInfo(video_url)
    for f in video_info['formats']:
        if f['ext']=='mp4':
            print("Audio Url Extracted...")
            return f['url']


if __name__=="__main__":
    video_url="https://www.youtube.com/watch?v=SC101xgx_Yc"
    audio_url=GetAudioUrl(video_url)
    print(audio_url)
