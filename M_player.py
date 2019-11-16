import pygame
import random, os
from os import path
import json,time

music_data = '/home/-/-/' # enter your music directory
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
		    pygame.mixer.music.load("/home/-/-/"+songs_list[x]) # enter your music directory
		    pygame.mixer.music.play(0)

		    # Wait for the music to play before exiting 
		    while pygame.mixer.music.get_busy():
		    	emoji=random.choice(emoji_list)
		    	time.sleep(2)
		        print(emoji.decode('unicode-escape'))
		        clock.tick(1)  	#This is class that will help us to track amount of time or to manage framerate.
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
	        pygame.mixer.music.load("/home/-/-/"+songs_list[x]) 	# enter your music directory
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
