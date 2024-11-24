import random


class MysteryTiles:
    def __init__(self, tiles, screen):
        self.tiles = tiles
        self.screen = screen

    def swap_tiles(self):
        # Get mystery tile id
        mystery_tile_id = None
        for tile in self.tiles:
            if tile["type"] == "mystery":
                mystery_tile_id = tile["id"]
                break

        # If no mystery tile is found, return the original screen
        if mystery_tile_id is None:
            return self.screen

        # Generate random index for swapping
        normal_tiles = [tile for tile in self.tiles if tile["type"] == "normal"]
        normal_tile_id = random.choice(normal_tiles)["id"]

        swapped_positions = [
            [
                1 if tile == mystery_tile_id else 0
                for tile in column
            ]
            for column in self.screen
        ]

        # Swap mystery tiles
        swapped_screen = [
            [
                normal_tile_id if tile == mystery_tile_id else tile
                for tile in column
            ]
            for column in self.screen
        ]

        return swapped_screen, swapped_positions, normal_tile_id
