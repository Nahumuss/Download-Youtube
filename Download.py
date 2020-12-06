from pytube import YouTube
from threading import Thread
from os import mkdir

def download_video(video_link, down_dir=""):
    try:
        tube = YouTube(video_link)
        title = tube.title
        print("Now downloading,  " + str(title))
        video = tube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print("FileSize : " + str(round(video.filesize/(1024*1024))) + 'MB')
        down_dir += "/" if down_dir != "" else ""
        try:
            mkdir(down_dir + str(title))
            video.download(down_dir + title)
        except:
            video.download(down_dir + "Others")
        print("Download complete")
        try:
            caption = tube.captions['en']
            subtitle = caption.generate_srt_captions()
            open(down_dir + title + "/" + title + '.srt', 'w').write(subtitle)
        except:
            print("No subtitles found")
    except Exception as e:
        print("ErrorDownloadVideo: \n")
        print(e)


def progress_function(stream,file_handle, bytes_remaining):
    pass #Thread(target=progress_prints, args=[stream,file_handle, bytes_remaining]).start()

def progress_prints(stream,file_handle, bytes_remaining):
    size = stream.filesize
    p = 0
    while p <= 100:
        print(str(p) + '%', end="\r")
        p = percent(size - bytes_remaining, size)

def percent(tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

if __name__ == "__main__":
    url = input("Enter video url: ")
    download_video(url, "Videos")