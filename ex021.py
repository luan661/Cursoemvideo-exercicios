import pygame
pygame.mixer.init()
pygame.mixer.pre_init()
a = pygame.mixer.Sound("xp.wav")
pygame.mixer.Sound.play(a)
