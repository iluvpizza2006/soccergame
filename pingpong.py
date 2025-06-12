import pygame
from timer import *
from PIL import Image
pygame.init()

width, height = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption
clock = pygame.time.Clock()

def load_image(name):
    image = pygame.image.load(name).convert_alpha()
    return image

ball_img = load_image("myachkrasivy.png")
fon_img = load_image("fonkrasivy (1).png")
stick1_img = load_image("palkakrutaya.png")
stick2_img = load_image("palkakrutaya.png")

player1 = pygame.Rect(50, height // 2 - stick1_img.get_height() // 2, stick1_img.get_width(), stick1_img.get_height())
player2 = pygame.Rect(50, height // 2 - stick1_img.get_height() // 2, stick1_img.get_width(), stick1_img.get_height())
ball = pygame.Rect(50, height // 2 - ball_img.get_height() // 2, ball_img.get_width(), ball_img.get_height())
fon = pygame.Rect(50, height // 2 - fon_img.get_height() // 2, fon_img.get_width(), fon_img.get_height())

#Игра ещё не работает!!! Game doesn't work yet!!!
