from pytube import YouTube
import re
import sys

def show_progress_bar(stream, _chunk, _file_handle, bytes_remaining):
    """this function shows the progress of the download operation
    in percent depending on the size of the video """
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()


def is_valid_link(link):
    """ it takes a link and return
    true if the link is valid and have the
    youtube link pattern """
    matcher = (
        r'(https?://)?(www\.)?'
         '(youtube|youtu|youtube-nocookie)\.(com|be)/'
         '(watch\?.*?(?=v=)v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    while True:
        valid_link = re.match(matcher,link)
        if valid_link :
            return  True
        else:
            return False


def select_streams(obj):
    """this function help us select between streams"""
    
    str_type = int(input("to see all the streams press 1 \nto see the aduio only streams press 2 : \n"))
    if str_type == 1 :
        st = obj.streams.all()
        return st
    elif str_type == 2 :
        st = obj.streams.filter(only_audio=True).all()
        return st



def show_streams(stre):
    stream_number = 1
    for x in stre:
        print(str(stream_number),x)
        stream_number += 1

url = str(input("copy a youtube url in here : "))
while True:
    if is_valid_link(url):
        yt = YouTube(url)
        break
    else:
        print("invalid link")
        url= str(input("copy a youtube url in here again : "))

yt.register_on_progress_callback(show_progress_bar)
selected_streams = select_streams(yt)
show_streams(selected_streams)


z=int(input("what stream do you want ???\n"))
stream = selected_streams[z-1]

print("You have chosen : \n" ,
      yt.title ,
      "\n",
      "with the stream :\n",
      stream,
      "\n",
      "please wait for the video to download")

stream.download()

print("every thing is done!!")
