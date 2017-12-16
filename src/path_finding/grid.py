class Grid:

    # TODO test this class

    def __init__(self, grid_array, simulation_size_x, simulation_size_y):
        self.grid = grid_array
        self.simulation_size_x = simulation_size_x
        self.simulation_size_y = simulation_size_y

    def is_walkable(self, x, y):
        if self.grid[y + (self.simulation_size_y // 2)][x + (self.simulation_size_x // 2)] == 255:
            return True
        else:
            return False
