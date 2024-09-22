import pygame, os
from typing import List
from pygame import Surface

BASE_URL = "assets/images/"


def load_image(url: str) -> Surface:
    """loads the image and clear transparent colorkey"""
    img = pygame.image.load(BASE_URL + url).convert()
    img.set_colorkey((0, 0, 0))
    return img


def load_images(url: str) -> List[Surface]:
    """gets a list of related images"""
    images = []
    for im in sorted(os.listdir(BASE_URL + url)):
        image = load_image(url + "/" + im)
        images.append(image)
    return images
