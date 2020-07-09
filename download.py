import requests
import urllib.request
import json
import ffmpeg


SAVE_PATH = r""

def get(submission):
    uf = urllib.request.urlopen(f"https://www.reddit.com/{submission}.json")
    html = uf.read()
    y = json.loads(html)
    url = str(y[0]["data"]["children"][0]["data"]["media"]["reddit_video"]["fallback_url"]).replace("?source=fallback","")
    video_url = url
    if ".mp4" in url:
        start = url.find("_")
        end = url[-6:].find(".")+len(url)

        if end == -1 or 0:
            audio_url = url.replace(url[start:],"_audio.mp4")
        else:
            audio_url = url.replace(url[start:end],"_audio.mp4")

    else:
        start = url[-10:].find("/")
        audio_url = url.replace(url[start+len(url)-10:],"/audio")
        

    return video_url, audio_url
    


def download(submission):
    urls = get(submission)
    video_url = urls[0]
    audio_url = urls[1]
    
    video_name = f"/video_{submission}.mp4"
    audio_name = f"/audio_{submission}.mp4"

    urllib.request.urlretrieve(video_url, SAVE_PATH+video_name)
    urllib.request.urlretrieve(audio_url, SAVE_PATH+audio_name)


    merge(submission)
def merge(submission):
    video_name = f"/video_{submission}.mp4"
    audio_name = f"/audio_{submission}.mp4"

    input_video = ffmpeg.input(SAVE_PATH+video_name)
    input_audio = ffmpeg.input(SAVE_PATH+audio_name)

    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(f"{SAVE_PATH}/final_{submission}.mp4").run()

