import requests

def Transcribe(audio_url,url,header):
    data={
        'audio_url':audio_url
    }
    result=requests.post(
        url,
        headers=header,
        json=data
    )
    if result.status_code==200:
        return (result.json()['id'],True)

    else:
        return (None,False)