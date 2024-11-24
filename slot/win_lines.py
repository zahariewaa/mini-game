class WinLines:
    def __init__(self, lines, pays, screen):
        self.lines = lines
        self.pays = pays
        self.screen = screen

    def get_win_lines(self):
        win_lines_list = []
        win_lines_counter = 0

        for line in self.lines:
            left_tile_id = self.screen[0][line[0]]
            left_length = 1

            for col in range(1, len(line)):
                if self.screen[col][line[col]] == left_tile_id:
                    left_length += 1
                else:
                    break

            min_length = min(
                pay[1] for pay in self.pays if pay[0] == left_tile_id
            )
            if left_length >= min_length:
                left_amount = next(
                    pay[2] / 10
                    for pay in self.pays
                    if pay[0] == left_tile_id and pay[1] == left_length
                )
                win_lines_list.append([left_tile_id, left_length, left_amount])
                win_lines_counter += 1

        return win_lines_list
