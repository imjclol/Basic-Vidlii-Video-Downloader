# Asking for Video Link
video = input("Inset Video Link: ")

# Downloads video page
import urllib.request
urllib.request.urlretrieve(video, "video.html")

# Defines "everything_between"
def everything_between(text,begin,end):
    idx1=content.find(begin)
    idx2=content.find(end,idx1)
    return content[idx1+len(begin):idx2].strip()

# Searches for video source
content = open('video.html').read()
videoLink = everything_between(content,'src: "','",')
videoTitle = everything_between(content,'<h1>','</h1>')

# Downloads video
title = videoTitle + ".mp4"
urllib.request.urlretrieve(videoLink, title)
print("Downloaded " + videoTitle)

# Deletes video page
import os
os.remove('video.html')