from __future__ import annotations
import pygame
from typing import TYPE_CHECKING, Iterable


if TYPE_CHECKING:
    from game import Game
    from src.tile import TileMap


class PhysicsBase:
    """Using this as my player blueprint for now"""

    def __init__(self, game: Game,tilemap: TileMap, c_type: str, pos: Iterable[int]) -> None:
        self.game = game
        self.tilmap = tilemap
        self.character_type = c_type
        self.position = list(pos)
        self.velocity = [0,0]


    def make_movement_frame(self,movement: tuple) -> None:
        """gets the movement delta
        movement param is from keypress"""
        frame_movement = (self.velocity[0] + movement[0] , self.velocity[1] + movement[1])
        self.velocity[1] = min(5, self.velocity[1] + 0.1) #terminal velocity
        self.position[0] += frame_movement[0]
        self.position[1] += frame_movement[1]


    def draw(self,surface: pygame.Surface) -> None:
        "draws the player"
        player = self.game.data["player"]
        surface.blit(player,self.position)

    
