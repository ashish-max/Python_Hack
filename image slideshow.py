import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((50, 50), pygame.FULLSCREEN)
sleep(3)
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()
sleep(2)
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()
image = pygame.image.load("mothersday.jpg")
window.blit(image, (0, 0))
pygame.display.update()
sleep(13)
