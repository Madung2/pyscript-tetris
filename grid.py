

class Grid:
    def __init__(self):
        self.num_rows  = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]

    
    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end=" ")
            print()

Grid().print_grid()
print(Grid().num_rows)

def check_import():
    a = 1+2
    return a
