import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from Extracting_text_from_video.Extracting_audio_from_video.get_audio_url import GetAudioUrl

def GetAudioFromUrl(video_url,audio_file):
    audio_url=GetAudioUrl(video_url)
    session=requests.Session()
    retry=Retry(total=5,backoff_factor=1,status_forcelist=[500,502,503,504])
    session.mount("http://",HTTPAdapter(max_retries=retry))
    session.mount("https://",HTTPAdapter(max_retries=retry))

    try:
        with session.get(audio_url,stream=True) as response:
            response.raise_for_status()
            with open(audio_file,"wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

        print(f"Audio file downloaded and saved as {audio_file}")

    except Exception as e:
        print(e)

    print("Audio file downloaded from url...")
    audio_file=os.path.join(os.getcwd(),audio_file)
    return audio_file



