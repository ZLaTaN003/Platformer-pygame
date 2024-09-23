from __future__ import annotations
from typing import List, TYPE_CHECKING
import random
from pygame import Surface
from src.utils import load_image

if TYPE_CHECKING:
    from game import Game


class Cloud:
    def __init__(self, game: Game, pos: List[int]) -> None:
        
        self.image = random.choice(
            (load_image("clouds/cloud_1.png"), load_image("clouds/cloud_2.png"))
        )
        self.pos = list(pos)

        self.game = game

    def make_move(self) -> None:
        self.pos[0] += 0.5 
        if self.pos[0] > self.game.screen_width:
            self.pos[0] = -220

    def draw(self, surface: Surface, offset: List[int]) -> None:
        surface.blit(self.image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))


def generate_clouds(number: int, game: Game, max_width, max_height) -> List[Cloud]:
    """generates some clouds"""
    clouds = []
    for _ in range(number):
        pos_x = random.randint(0 - 220, max_width - 1)

        pos_y = random.randint(0 - 220, max_height - 1)
        cloud = Cloud(game=game, pos=[pos_x, pos_y])
        clouds.append(cloud)

    return clouds
