from gtts import gTTS
import time
import pygame
from pygame.locals import *

text = '''  I am speaking in english US. Happy that he found some water finally, he swooped down to the tree and then down to the ground. He quickly moved towards the pitcher and looked inside. There was very little water in the pot. The crow put his beak inside the pitcher but could not reach the water. The water level was too low, and the narrow opening prevented his neck from going all the way down.'''

language = 'en-us'
speech = gTTS(text = text, lang = language, slow = False)
speech.save("text.mp3")
pygame.mixer.init()
pygame.mixer.music.load("text.mp3")
pygame.mixer.music.set_volume(0.9)
pygame.mixer.music.play()
time.sleep(15)
#pygame.mixer.music.stop()


#os.system("mpg321 text.mp3")
