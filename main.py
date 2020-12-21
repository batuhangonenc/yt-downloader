import pytube,sys,os

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()

print("----------\nYoutube Downloader\n\n1 - download a video\nq - quit")

while 1:
	i1 = input("choose one :")

	if i1 == "q":
		sys.exit()

	elif i1 == "1":
		url = input("enter a url :")
		
		fname = input("enter a filename :")
		

		try:
			youtube = pytube.YouTube(url)
			video = youtube.streams.get_highest_resolution()

			video.download(filename=fname)


			print("--\nyou downloaded a file :\n{}\ncheck your folder.".format(url))
		except:
			print("--\nsomething went wrong with url.")
			continue

	else:
		print("--\nunvalid input")
