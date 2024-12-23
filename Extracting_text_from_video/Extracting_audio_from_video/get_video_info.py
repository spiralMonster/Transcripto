import yt_dlp

def GetVideoInfo(video_url):
    y=yt_dlp.YoutubeDL()
    with y:
        result=y.extract_info(
            video_url,
            download=False
        )
    if 'entries' in result:
        return result['entries'][0]

    return result

if __name__=='__main__':
    video_url="https://www.youtube.com/watch?v=mYUyaKmvu6Y"
    result=GetVideoInfo(video_url)
    print(result)