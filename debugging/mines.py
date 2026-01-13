#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        if mines >= width * height:
            raise ValueError("Number of mines must be less than number of cells.")
        self.width = width
        self.height = height
        self.mines_set = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_mine(self, x, y):
        return (y * self.width + x) in self.mines_set

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue  # don't count the cell itself
                nx, ny = x + dx, y + dy
                if self.in_bounds(nx, ny) and self.is_mine(nx, ny):
                    count += 1
        return count

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if self.is_mine(x, y):
                        print('*', end=' ')
                    else:
                        c = self.count_mines_nearby(x, y)
                        print(c if c > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def reveal(self, x, y):
        if not self.in_bounds(x, y):
            print("Out of bounds. Try again.")
            input("Press Enter to continue...")
            return True  # not a loss, just ignore

        if self.revealed[y][x]:
            return True  # already revealed; ignore

        if self.is_mine(x, y):
            return False

        # flood fill using stack to avoid recursion depth issues
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if not self.in_bounds(cx, cy) or self.revealed[cy][cx]:
                continue
            if self.is_mine(cx, cy):
                continue

            self.revealed[cy][cx] = True

            if self.count_mines_nearby(cx, cy) == 0:
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = cx + dx, cy + dy
                        if self.in_bounds(nx, ny) and not self.revealed[ny][nx]:
                            stack.append((nx, ny))
        return True

    def has_won(self):
        # win if all non-mine cells are revealed
        total_cells = self.width * self.height
        revealed_count = sum(1 for row in self.revealed for v in row if v)
        return revealed_count == (total_cells - len(self.mines_set))

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if self.has_won():
                    self.print_board(reveal=True)
                    print("🎉 You win! All safe cells revealed.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
