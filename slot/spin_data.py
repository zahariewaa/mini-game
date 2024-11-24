import json
import random
from slot.mystery_tiles import MysteryTiles
from slot.win_lines import WinLines


class SpinData:
    ROWS = 3

    @staticmethod
    def get_config():
        with open("src/config.json", "r") as file:
            return json.load(file)

    @staticmethod
    def get_indexes(reels):
        indexes = [random.randint(0, len(reel) - 1) for reel in reels]
        return indexes

    @staticmethod
    def spin():
        config = SpinData.get_config()
        reels = config["reels"][0]
        cols = len(reels)

        indexes = SpinData.get_indexes(reels)
        screen = []

        # Generate the visible screen
        for col in range(cols):
            row = [
                reels[col][(indexes[col] + i) % len(reels[col])]
                for i in range(SpinData.ROWS)
            ]
            screen.append(row)

        print("Initial Screen:")
        print(screen)

        tiles = config["tiles"]
        swap_tiles = MysteryTiles(tiles, screen)
        swapped_screen, swap_tiles_mask, swapped_tile_id = swap_tiles.swap_tiles()

        print("Swapped Tile ID:", swapped_tile_id)
        print("Swap Tiles Mask:")
        print(swap_tiles_mask)

        lines = config["lines"]
        pays = config["pays"]

        print("Final Screen:")
        print(swapped_screen)
        win_lines = WinLines(lines, pays, swapped_screen)
        win_lines_list = win_lines.get_win_lines()

        print("Winning Lines:")
        print(win_lines_list)

        win_lines_amount = sum(win_line[2] for win_line in win_lines_list)
        print("Total Win Amount:", win_lines_amount)
