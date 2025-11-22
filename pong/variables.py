import pygame
import os
import json
pygame.init()
current_directory = os.getcwd()
clock = pygame.time.Clock()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h))
with open("{}\\settings.json".format(current_directory), 'r') as file:
    settings = json.load(file)
    file.close()