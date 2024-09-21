import pygame,os

BASE_URL = "assets/images/"

def load_image(url):
    """loads the image and clear transparent colorkey"""
    img = pygame.image.load(BASE_URL + url).convert()
    img.set_colorkey((0,0,0))
    return img


