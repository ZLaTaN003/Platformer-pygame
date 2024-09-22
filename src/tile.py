from __future__ import annotations
import pygame
from typing import TYPE_CHECKING
from pygame import Surface


if TYPE_CHECKING:
    from game import Game


class TileMap:
    def __init__(self, game: Game, tile_size: int = 16) -> None:
        self.game = game
        self.tile_size = tile_size
        self.tilemap = (
            {}
        )  # stores the  tile with its types its index of img list pos of grid column and row

        for i in range(10): #grid of tilemap
            self.tilemap[(3 + i, 10)] = {
                "type": "grass",
                "index": 1,
                "pos": (3 + i, 10),  # grid position
            }  # horizontal grass line as tile_loc : tile_data  l
            self.tilemap[(10, 3 + i)] = {
                "type": "stone",
                "index": 1,
                "pos": (10, 3 + i),  # grid position
            }  # vertical stone line as tile_loc : tile_data  l

    def draw(self, surface: Surface) -> None:
        for tile_loc in self.tilemap:  # gets tile locs
            tile = self.tilemap[tile_loc]  # tile data dict
            surface.blit(
                self.game.data[tile["type"]][tile["index"]],
                (
                    tile["pos"][0] * self.tile_size,
                    tile["pos"][1] * self.tile_size,
                ),  # multiply with tile_size so each tile takes its size
            )

    def find_neighbour_tiles(self, pos: tuple):
        """Find all the neighbouring tiles  takes in position which was multiplied by size"""

        tile_pos = (
            int(pos[0] // self.tile_size),
            int(pos[1] // self.tile_size),
        )  # gets  grid position
        neighbour_offsets = [
            (0, 0),
            (0, 1),
            (0, -1),
            (1, 0),
            (1, 1),
            (1, -1),
            (-1, 0),
            (-1, 1),
            (-1, -1),
        ]  # permutation for all possible neighbour for given cell

        neighbours = []
        for neighbour_offset in neighbour_offsets:
            neighbour_tile_pos = (
                tile_pos[0] + neighbour_offset[0],
                tile_pos[1] + neighbour_offset[1],
            )
            if neighbour_tile_pos in self.tilemap:
                neighbours.append(self.tilemap[neighbour_tile_pos])

        return neighbours

    def collision_tile_rects(self, pos: tuple):
        """Gets a list of tile rects for collision"""
        tile_rects = []
        for neighbour_tile in self.find_neighbour_tiles(pos):
            if neighbour_tile["type"] in ("grass", "stone"):
                tile_rects.append(
                    pygame.Rect(
                        neighbour_tile["pos"][0] * self.tile_size,  #each tile takes its pixel position
                        neighbour_tile["pos"][1] * self.tile_size,
                        self.tile_size,                             #size of tile rect
                        self.tile_size,
                    )
                )

        return tile_rects
