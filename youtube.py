import sys
import os	
import time
import update as up

sys.path.append("/home/david/.local/bin/vlc")
sys.path.append("/home/david/.local/bin/pytube")

import pytube as pt
import vlc

# get playlist and set resolution 
playlist = pt.Playlist('https://youtube.com/playlist?list=PLwM5hMwNTYGa2V4v4Q9ZYUFDp9dmo6tgO')
resolution = "1080p"

# initialize filename and player object
filename = None
player = None


	
# download video new video function
def download_video():
	global filename, player
	
	if len(os.listdir('/home/david/YouTubePlayer/videos')) != 0:
		os.system('rm /home/david/YouTubePlayer/videos/*')
	
	# obtaining the first video URL in the playlist
	vid_url = playlist.video_urls[0]
	
	# download video at desired resolution in videos folder
	youtube = pt.YouTube(vid_url)
	
	video = youtube.streams.get_highest_resolution()
	filename = video.download("videos")
	print(filename)
	
	
def play_video():
	global filename
	
	os.system(f'mplayer -fs -loop 0 -ao alsa \"{filename}\"')


def main():
	global player

	# download the first video in the playlist
	download_video()
	
	
	play_video()
			

main()
