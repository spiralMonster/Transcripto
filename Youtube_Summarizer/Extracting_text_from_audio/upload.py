import requests

def read_file(filename,chunk_size=5242880):
    with open(filename,'rb') as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data


def Upload(file,url,headers):
    data=read_file(file)
    result=requests.post(
        url,
        headers=headers,
        data=data
    )
    if result.status_code==200:
        return (result.json()['upload_url'],True)

    else:
        return (None,False)

