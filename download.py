import json
import urllib.request



def download(submission_id, path):
    uf = urllib.request.urlopen(f"https://www.reddit.com/{submission_id}.json")
    html = uf.read()
    y = json.loads(html)
    url = str(y[0]["data"]["children"][0]["data"]["media"]["reddit_video"]["fallback_url"]).replace("?source=fallback","")
    x = url[-6:].find(".")
    file_format = url[-6:][x:]
    name = f'{submission_id}{file_format}'
    urllib.request.urlretrieve(url, path+name)


