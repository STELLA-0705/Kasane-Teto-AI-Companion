import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load(r"C:\Users\janey\OneDrive\Desktop\Teto AI Companion\welcome_back_Track1.wav")

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(0.1)