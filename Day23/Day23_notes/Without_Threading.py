
import requests
import time

urls=[
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.amazon.com",
    "https://www.flikart.com"
]

def download_file(url):
    try:
        response=requests.get(url)
        filename=url.split("/")[-1]+".txt"
        
        with open(filename,"w",encoding="utf-8") as f:
            f.write(response.text)
        print(f"Downloaded:{filename}")
    except Exception as e:
        print(f"Error downloading {url} :{e}")
        
starttime=time.time()
for url in urls:
    download_file(url)
sequentialtime=time.time()-starttime
print(f"sequentialtime download time:{sequentialtime}")
