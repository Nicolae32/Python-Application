
from moviepy.editor import VideoFileClip

def convert(file):
    v = VideoFileClip(filename=file)
    v.audio.write_audiofile(file[:-4] + '.mp3')
    v.close()
 
while True:

    file = input()
    if file =="stop":
        break
    else:
        convert(file)
 
 

