import requests
import os
from Extracting_text_from_video.Extracting_audio_from_video.get_audio_from_url import GetAudioFromUrl


def preprocess_m3u(filepath):
    with open(filepath,'r') as file:
        lines=file.readlines()

    media_files=[]
    for line in lines:
        line=line.strip()
        if line and not line.startswith("#"):
            media_files.append(line)

    return media_files


def download_media(url,filepath):
    response=requests.get(url,stream=True)
    if response.status_code==200:
        with open(filepath,"ab") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

    else:
        print(f"Failed to download file from {url}")




def preprocess_to_mp3(input_file,output_file):
    media_files=preprocess_m3u(input_file)
    for media in media_files:
        if media.startswith("http"):
            download_media(media,output_file)

        else:
            print(f"Skipping download:{media}")

    print(f"Mp3 file stored at:{output_file}")
    return output_file

def ConvertingAudioToMp3(video_url):
    input_file="audio.m3u"
    output_file="audio2.mp3"
    input_file=GetAudioFromUrl(video_url,input_file)
    output_file=preprocess_to_mp3(input_file,output_file)
    os.remove(input_file)
    print("Audio Converted to Mp3 file...")
    output_file=os.path.join(os.getcwd(),output_file)
    return output_file


