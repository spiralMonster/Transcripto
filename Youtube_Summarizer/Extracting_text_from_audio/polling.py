import requests
import time

def Polling(url,header):
    while True:
        result=requests.get(
            url,
            headers=header
        )
        if result.status_code==200:
            status=result.json()['status']
            if status=='completed':
                return result
        print("Waiting for audio transcripting")
        time.sleep(60)