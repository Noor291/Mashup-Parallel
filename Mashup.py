import threading 
import time
import os
import sys
from pytube import Search
from pytube import YouTube
import moviepy.editor as mp
import glob
from youtube_search import YoutubeSearch
import multiprocessing


def task(y,i,duration):
    youtubeObject = YouTube(y)
    youtubeObject = youtubeObject.streams.get_highest_resolution().download(
    output_path='Videos', filename=f"video{i+1}.mp4")
    print(f"Downloaded video {i+1}")
    clip = mp.VideoFileClip(f"Videos/video{i+1}.mp4").subclip(0, duration)
    clip.audio.write_audiofile(f"Audios/audio{i+1}.mp3")
        

def makeMashup(output):
    dir_path = 'Audios/'
    count = 0

    for path in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    audio_clips = [mp.AudioFileClip(
        f"Audios/audio{i+1}.mp3") for i in range(0, count)]
    final_clip = mp.concatenate_audioclips(audio_clips)
    final_clip.write_audiofile(output)


if __name__ == "__main__":
    if (len(sys.argv) != 5):
        print("ERROR: Number of arguments are not correct")
        exit()
    n=int(sys.argv[2])
    x=sys.argv[1]
    duration=int(sys.argv[3])
    output=sys.argv[4]
    numberOfCores = multiprocessing.cpu_count()
    if n<=10:
        print("ERROR: Number of videos should be more than 10.")
        exit()
    if n!=numberOfCores:
        print("NOTE: Number of videos to be entered should be equal to number of cores in your machine for optimal run time, nonethless the code will run")
    if duration<20 and duration>90:
        print("ERROR: Duration of the audio must be between 20 and 90 seconds.")
        exit()
    if not output.endswith(".mp3"):
        print("ERROR:{} is not an mp3 file.".format(output))
        exit()
    
       
    results = YoutubeSearch(x, max_results=n).to_dict()
    if not os.path.exists("Videos"):
        os.mkdir("Videos")
    if not os.path.exists("Audios"):
        os.mkdir("Audios")

    
    startTime = time.time()

    numberOfThreads = n

    activeThreads = threading.activeCount()
    print("Program Started....")

    for i, result in enumerate(results):
        video_url = "https://www.youtube.com/watch?v=" + result["id"]
        t = threading.Thread(target=task , args=(video_url,i,duration,))
        t.start()
        while True:
            if threading.activeCount() - activeThreads + 1 <= numberOfThreads:
                break
            time.sleep(1)

    while True:
        if threading.activeCount() == activeThreads+1:
            break
        else:
            print ("    Thread still running (%d)..."%(threading.activeCount() - activeThreads))
            time.sleep(1)
    makeMashup(output)
    
    