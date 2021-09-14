# A simple Python program using backtracking to solve the Sudoku problem

class Grid:
    LENGTH = 9  # Default Sudoku board size

    def __init__(self, grid):
        self.grid = grid

    # A function to print the grid
    def print_grid(self):
        for i in range(Grid.LENGTH):
            for j in range(Grid.LENGTH):
                print(str(self.grid[i][j]) + '{}'.format(' '), end='')
            print('\n', end='')

    # Checks whether it is possible ot insert value to the given row, col
    # Returns a bool which indicates whether it is legal or not
    def check_position_is_safe(self, row: int, col: int, value: int):
        return not self.present_in_row(row, value) and not self.present_in_col(col,
                                                                               value) and not self.present_in_sector(
            row - row % 3, col - col % 3, value)

    # Returns a bool which indicates whether value is contained in the given row
    def present_in_row(self, row: int, value: int) -> bool:
        for i in range(self.LENGTH):
            if self.grid[row][i] == value:
                return True
        return False

    # Returns a bool which indicates whether value is contained in the given col
    def present_in_col(self, col: int, value: int) -> bool:
        for i in range(self.LENGTH):
            if self.grid[i][col] == value:
                return True
        return False

    # Returns a bool which indicates whether value is contained in the given row, col
    def present_in_sector(self, row: int, col: int, value: int) -> bool:
        for i in range(int(self.LENGTH / 3)):
            for j in range(int(self.LENGTH / 3)):
                if self.grid[i + row][j + col] == value:
                    return True
        return False

    # Function to find an empty spot in the grid
    # assigning found position col, row values
    # to row_col_record
    def find_empty_position(self, row_col_record):
        for i in range(self.LENGTH):
            for j in range(self.LENGTH):
                if self.grid[i][j] == 0:
                    row_col_record[0] = i
                    row_col_record[1] = j
                    return True
        return False

    def solve(self):
        row_col_record = [0, 0]

        if not self.find_empty_position(row_col_record):
            return True

        row = row_col_record[0]
        col = row_col_record[1]

        for num in range(1, 10):
            if self.check_position_is_safe(row, col, num):
                self.grid[row][col] = num

                if self.solve():
                    return True

                self.grid[row][col] = 0

        return False


def main():
    grid = Grid([[3, 0, 6, 5, 0, 8, 4, 0, 0],
                 [5, 2, 0, 0, 0, 0, 0, 0, 0],
                 [0, 8, 7, 0, 0, 0, 0, 3, 1],
                 [0, 0, 3, 0, 1, 0, 0, 8, 0],
                 [9, 0, 0, 8, 6, 3, 0, 0, 5],
                 [0, 5, 0, 0, 9, 0, 6, 0, 0],
                 [1, 3, 0, 0, 0, 0, 2, 5, 0],
                 [0, 0, 0, 0, 0, 0, 0, 7, 4],
                 [0, 0, 5, 2, 0, 6, 3, 0, 0]])

    if grid.solve():
        grid.print_grid()
    else:
        print("No solution exists")


if __name__ == "__main__":
    main()
