from __future__ import annotations
import pygame
from typing import TYPE_CHECKING, Iterable, List


if TYPE_CHECKING:
    from game import Game
    from src.tile import TileMap


class PhysicsBase:
    """Using this as my player blueprint for now"""

    def __init__(
        self, game: Game, tilemap: TileMap, c_type: str, pos: Iterable[int]
    ) -> None:
        self.game = game
        self.tilemap = tilemap
        self.character_type = c_type
        self.position = list(pos)
        self.velocity = [0, 0]
        self.size = (8, 15)

    def make_movement_frame(self, movement: tuple) -> None:
        """gets the movement delta
        movement param is from keypress"""
        frame_movement = (
            self.velocity[0] + movement[0],
            self.velocity[1] + movement[1],
        )

        self.position[0] += frame_movement[0]

        player_rect = self.rect()
        for tile_rect in self.tilemap.collision_tile_rects(self.position):
            if player_rect.colliderect(tile_rect):
                if frame_movement[0] > 0:  # moves right +ve value of movement
                    player_rect.right = (
                        tile_rect.left
                    )  # makes collision possible by changing the player_rect and tile_rect sides
                if frame_movement[0] < 0:  # move left -ve
                    player_rect.left = tile_rect.right
                self.position[0] = (
                    player_rect.x
                )  # change position of player to new position

        self.position[1] += frame_movement[1]
        player_rect = self.rect()
        for tile_rect in self.tilemap.collision_tile_rects(self.position):
            if player_rect.colliderect(tile_rect):
                if frame_movement[1] > 0:  # moves down +ve value of movement
                    player_rect.bottom = tile_rect.top  # makes collision possible
                    self.velocity[1] = 0
                if frame_movement[1] < 0:  # move up -ve
                    player_rect.top = tile_rect.bottom
                self.position[1] = player_rect.y

        self.velocity[1] = min(5, self.velocity[1] + 0.1)  # terminal velocity

    def draw(self, surface: pygame.Surface, offset: List[int]) -> None:
        "draws the player"
        player = self.game.data["player"]
        surface.blit(
            player, (self.position[0] - offset[0], self.position[1] - offset[1])  #subtract camera offset which make it moving
        )

    def rect(self):
        """player rect"""
        return pygame.Rect(
            self.position[0], self.position[1], self.size[0], self.size[1]
        )
