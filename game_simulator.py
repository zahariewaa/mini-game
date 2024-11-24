import random
from slot.spin_data import SpinData
from slot.mystery_tiles import MysteryTiles  # Import MysteryTiles
from slot.win_lines import WinLines  # Import WinLines


class GameSimulator:
    def __init__(self, spins, bet_per_spin, batch_size):
        self.spins = spins
        self.bet_per_spin = bet_per_spin
        self.batch_size = batch_size
        self.total_bet = 0
        self.total_winnings = 0
        self.winning_spins = 0

    def simulate(self):
        num_batches = (self.spins + self.batch_size - 1) // self.batch_size  # Ceiling division

        for batch in range(num_batches):
            spins_in_batch = min(self.batch_size, self.spins - (batch * self.batch_size))
            print(f"Processing batch {batch + 1} of {num_batches} with {spins_in_batch} spins...")
            for _ in range(spins_in_batch):
                self.total_bet += self.bet_per_spin
                winnings = self.simulate_spin()
                self.total_winnings += winnings
                if winnings > 0:
                    self.winning_spins += 1

    def simulate_spin(self):
        # Use SpinData to simulate a single spin
        config = SpinData.get_config()
        reels = config["reels"][0]
        tiles = config["tiles"]
        lines = config["lines"]
        pays = config["pays"]

        indexes = SpinData.get_indexes(reels)
        screen = [
            [reels[col][(indexes[col] + i) % len(reels[col])] for i in range(SpinData.ROWS)]
            for col in range(len(reels))
        ]

        # Handle mystery tiles
        mystery_tiles = MysteryTiles(tiles, screen)
        swapped_screen, _, _ = mystery_tiles.swap_tiles()

        # Calculate winnings
        win_lines = WinLines(lines, pays, swapped_screen)
        win_lines_list = win_lines.get_win_lines()
        total_win_amount = sum(win_line[2] for win_line in win_lines_list)

        return total_win_amount

    def calculate_rtp(self):
        return (self.total_winnings / self.total_bet) * 100

    def calculate_hit_rate(self):
        return (self.winning_spins / self.spins) * 100

    def calculate_win_rate(self):
        return self.total_winnings / self.spins

    def report(self):
        rtp = self.calculate_rtp()
        hit_rate = self.calculate_hit_rate()
        win_rate = self.calculate_win_rate()

        print(f"\nSimulation Report:")
        print(f"Total Spins: {self.spins}")
        print(f"Total Bet: {self.total_bet}")
        print(f"Total Winnings: {self.total_winnings}")
        print(f"Winning Spins: {self.winning_spins}")
        print(f"RTP: {rtp:.2f}%")
        print(f"Hit Rate: {hit_rate:.2f}%")
        print(f"Win Rate: {win_rate:.2f}")


if __name__ == "__main__":
    # Example parameters
    TOTAL_SPINS = 1000000
    BET_PER_SPIN = 1  # Example bet amount
    BATCH_SIZE = 10000  # Number of spins processed per batch

    simulator = GameSimulator(TOTAL_SPINS, BET_PER_SPIN, BATCH_SIZE)
    simulator.simulate()
    simulator.report()
