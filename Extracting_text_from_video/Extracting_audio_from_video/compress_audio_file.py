from pydub import AudioSegment
import os
from Extracting_text_from_video.Extracting_audio_from_video.converting_audio_to_mp3 import ConvertingAudioToMp3

def CompressAudioFile(video_url,speed_factor=1.5):
    audio_file=ConvertingAudioToMp3(video_url)

    audio=AudioSegment.from_file(audio_file)
    faster_audio=audio._spawn(
        audio.raw_data,
        overrides={
            'frame_rate':int(audio.frame_rate*speed_factor)
        }
    ).set_frame_rate(audio.frame_rate)
    filepath="audio_final.mp3"
    faster_audio.export(filepath)
    os.remove(audio_file)
    print("Final Audio file is extracted....")
    filepath=os.path.join(os.getcwd(),filepath)
    return filepath

