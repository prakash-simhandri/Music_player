# import pygame  
# import time
# file = '/home/pandu/Desktop/my_data/AI/spwch_work/I Got You.mp3'
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load(file)
# pygame.mixer.music.play()
# time.sleep(20)
# pygame.mixer.music.pause()
# time.sleep(5)
# pygame.mixer.music.unpause()
# pygame.event.wait()


# ============================

import pygame # sudo apt install libsdl2-dev libfreetype6-dev libsdl2-mixer-dev libsdl2-image-dev libsdl2-ttf-dev libjpeg-dev libpng-dev libportmidi-dev
import random, os
from os import path
import json,time

music_data = '/home/pandu/Music/Englesh_songs' # enter your music directory
songs_list = os.listdir(music_data)
x= 0
if path.exists("Emoji.json"):
	with open("Emoji.json","r")as open_file:
		emoji_list=json.load(open_file)
else:
	print("sorry sir Emoji file is not exists : plisse run the emoji.json.py file")

try:
	def music():
		global x, c
		try:	
		    pygame.init()
		    pygame.mixer.init()
		    clock = pygame.time.Clock()
		    pygame.mixer.music.load("/home/pandu/Music/Englesh_songs/"+songs_list[x]) # enter your music directory
		    pygame.mixer.music.play(0)

		    # Wait for the music to play before exiting 
		    while pygame.mixer.music.get_busy():
		    	emoji=random.choice(emoji_list)
		    	time.sleep(2)
		        print(emoji.decode('unicode-escape'))
		        clock.tick(1)  #This is class that will help us to track amount of time or to manage framerate.
		    que()
		except Exception as e:
			user_choice=raw_input({e:"Do you want listening again: YES/NO >>"})
			if user_choice == "yes":
				x=0
				music()
			else:
				print("Ok sir by")

	def stop_music():
   		pygame.mixer.music.stop()


	def que():
	    global x, songs_list
	    pos = pygame.mixer.music.get_pos()
	    if int(pos) == -1:
	        x += 1
	        clock = pygame.time.Clock()
	        pygame.mixer.music.load("/home/pandu/Music/Englesh_songs/"+songs_list[x]) # enter your music directory
	        pygame.mixer.music.play(0)
	        
	        # Wait for the music to play before exiting 
	        while pygame.mixer.music.get_busy():
	        	emoji=random.choice(emoji_list)
	        	time.sleep(2)
		        print(emoji.decode('unicode-escape'))
	        	clock.tick(1)
	        x += 1
	        music()
	music()
except KeyboardInterrupt:	# to stop playing, press "ctrl-c"
    stop_music()

except Exception as error:
    print(error)