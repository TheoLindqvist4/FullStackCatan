import random

class Player:
    player_ressources = {
        'Ore': 0,  
        'Weat': 0, 
        'Sheep': 0,  
        'Brick': 0,
        'Wood': 0 
    }
    player_dev_cards = {
        'Knight': 0,  
        'Year of plenty': 0, 
        'Monopoly': 0,  
        'Road builder': 0,
        'Victory Point': 0 
    }
    player_points = 0
    player_settlement = 5
    player_cities = 4
    player_roads = 15

    player_longest_road = False
    player_army = False

    player_ore_port = False
    player_weat_port = False
    player_sheep_port = False
    player_brick_port = False
    player_wood_port = False
    player_3_to_1_port = False

class Board:
    def __init__(self):
        self.numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.rows = [3, 4, 5, 4, 3]  # 3-4-5-4-3 pattern for row lengths
        self.grid = []  # Stores numbers on each tile
        self.tile_grid = []  # Stores tile types on each tile
        self.tiles = {
            'Ore': 3,  
            'Weat': 4, 
            'Sheep': 4,  
            'Brick': 3,
            'Wood': 4,
            'Desert': 1
        }
        self.generate_board()
        self.assign_tiles()

    def is_adjacent_valid(self, row, col, num):
        if num in self.get_adjacent(row, col):
            return False
        if num == 2 and 12 in self.get_adjacent(row, col):
            return False
        if num == 12 and 2 in self.get_adjacent(row, col):
            return False
        if num == 8 and 6 in self.get_adjacent(row, col):
            return False
        if num == 6 and 8 in self.get_adjacent(row, col):
            return False
        return True

    def get_adjacent(self, row, col):
        adjacents = []
        # Adjacent positions based on hexagonal layout
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[r]):
                adjacents.append(self.grid[r][c])
        return adjacents

    def generate_board(self):
        # Initialize the grid with empty slots following the 3-4-5-4-3 structure
        self.grid = [[] for _ in range(5)]
        numbers = self.numbers[:]
        random.shuffle(numbers)
        
        for row, row_length in enumerate(self.rows):
            for col in range(row_length):
                for num in numbers:
                    if self.is_adjacent_valid(row, col, num):
                        self.grid[row].append(num)
                        numbers.remove(num)
                        break

    def assign_tiles(self):
        # Initialize an empty grid for tiles following the 3-4-5-4-3 structure
        self.tile_grid = [[] for _ in range(5)]
        
        # Find the location of the number 7 and assign the Desert tile there
        tile_counts = self.tiles.copy()
        for row in range(5):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 7:
                    self.tile_grid[row].append('Desert')
                    tile_counts['Desert'] -= 1
                else:
                    self.tile_grid[row].append(None)  # Placeholder for other tiles

        # Flatten available tile positions for easier assignment
        tile_positions = [(r, c) for r in range(5) for c in range(len(self.grid[r])) if self.tile_grid[r][c] is None]
        tile_types = [tile for tile, count in tile_counts.items() for _ in range(count)]
        random.shuffle(tile_types)

        # Assign remaining tiles randomly
        for (row, col), tile_type in zip(tile_positions, tile_types):
            self.tile_grid[row][col] = tile_type

    def display_board(self):
        for num_row, tile_row in zip(self.grid, self.tile_grid):
            row_display = " ".join(f"{num}({tile})" for num, tile in zip(num_row, tile_row))
            print(row_display)

class Deck:
    resource_ore = 21
    resource_weat = 21
    resource_sheep = 21
    resource_brick = 21
    resource_wood = 21



    
class Dice:
    dice_value = 6

    def roll_dice(self):
        self.dice_value = random.randint(1,6)
        return self.dice_value

    def print_value(self):
        return print(self.dice_value)
    
dice_1 = Dice()
dice_2 = Dice()
dice_1.roll_dice()
dice_2.roll_dice()
dice_1.print_value()
dice_2.print_value()
total_dice = dice_1.dice_value + dice_2.dice_value
print(total_dice)


class Stats:
    number_of_knights = 0


class Game_4_players:
    player_order = [1, 2, 3, 4]
    
    def __init__(self):
        # Create player instances
        self.players = {
            1: Player(),
            2: Player(),
            3: Player(),
            4: Player()
        }
        self.randomize_order()
        
    def randomize_order(self):
        random.shuffle(self.player_order)

    def placing_first_settlement(self):
        for player_num in self.player_order:
            player = self.players[player_num]
            
            # Player places a settlement
            if player.player_settlement > 0:
                player.player_settlement -= 1
                print(f"Player {player_num} placed a settlement. Remaining settlements: {player.player_settlement}")
            
            # Player places a road
            if player.player_roads > 0:
                player.player_roads -= 1
                print(f"Player {player_num} placed a road. Remaining roads: {player.player_roads}")

    def print_order(self):
        print("Player turn order:", self.player_order)

# Example usage:
game = Game_4_players()
game.print_order()  # Shows the randomized player order
game.placing_first_settlement()  # Players take turns placing settlements and roads


import tkinter as tk
from PIL import Image, ImageTk

import tkinter as tk
from PIL import Image, ImageTk

class CatanInterface:
    def __init__(self, board):
        self.board = board
        self.root = tk.Tk()
        self.root.title("Catan Board")

        # Paths to resources and numbers
        self.resource_images = {
            'Brick': "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/tiles/brick.png",
            'Sheep': "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/tiles/sheep.png",
            'Ore': "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/tiles/stone.png",
            'Weat': "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/tiles/weat.png",
            'Wood': "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/tiles/wood.png",
            'Desert': "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/tiles/desert.png"
        }
        self.number_images = {
            2: "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/numbers/2.png",
            3: "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/numbers/3.png",
            4: "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/numbers/4.png",
            5: "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/numbers/5.png",
            6: "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/numbers/6.png",
            8: "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/numbers/8.png",
            9: "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/numbers/9.png",
            10: "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/numbers/10.png",
            11: "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/numbers/11.png",
            12: "C:/Theo/School/ESIEE/Annee/E5/Full Stack/First version Catan/images/numbers/12.png"
        }

        self.load_images()
        self.create_board()
        self.root.mainloop()

    def scale_dimensions(self, scale_of_widget):
        dimension_image = [298,345]
        new_dimension = [
            scale_of_widget[0] - 100,
            scale_of_widget[1] - 100
        ]

        scale_image = new_dimension[0] / 5
        scale_image_overlap = scale_image * 1.3245

        factor = scale_image_overlap / dimension_image[1]
        new_dimension_image = [
            dimension_image[0] * factor,
            dimension_image[1] * factor
        ]

        # Calculate positions based on new dimensions
        positions = {
            1: [
                [new_dimension[0] / 2 - new_dimension_image[0],0],
                [new_dimension[0] / 2, 0],
                [new_dimension[0] / 2 + new_dimension_image[0], 0]
            ],
            2: [
                [new_dimension[0] / 2 - 1.5 * new_dimension_image[0], scale_image],
                [new_dimension[0] / 2 - new_dimension_image[0] / 2, scale_image],
                [new_dimension[0] / 2 + new_dimension_image[0] / 2, scale_image],
                [new_dimension[0] / 2 + 1.5 * new_dimension_image[0],scale_image]
            ],
            3: [
                [new_dimension[0] / 2 - 2 * new_dimension_image[0], 2* scale_image],
                [new_dimension[0] / 2 - new_dimension_image[0], 2*scale_image],
                [new_dimension[0] / 2, 2*scale_image],
                [new_dimension[0] / 2 + new_dimension_image[0], 2*scale_image],
                [new_dimension[0] / 2 + 2 * new_dimension_image[0], 2*scale_image]
            ],
            4: [
                [new_dimension[0] / 2 - 1.5 * new_dimension_image[0], 3*scale_image],
                [new_dimension[0] / 2 - new_dimension_image[0] / 2, 3*scale_image],
                [new_dimension[0] / 2 + new_dimension_image[0] / 2, 3*scale_image],
                [new_dimension[0] / 2 + 1.5 * new_dimension_image[0], 3*scale_image]
            ],
            5: [
                [new_dimension[0] / 2 - new_dimension_image[0], 4*scale_image],
                [new_dimension[0] / 2, 4*scale_image],
                [new_dimension[0] / 2 + new_dimension_image[0], 4*scale_image]
            ]
        }

        return new_dimension_image, positions



    def load_images(self):
        scale_of_widget = [800, 800]
        self.tile_size, self.positions = self.scale_dimensions(scale_of_widget)
        
        # Resize tile and number images based on scaled dimensions
        self.tile_imgs = {
            key: ImageTk.PhotoImage(Image.open(path).resize((int(self.tile_size[0]), int(self.tile_size[1])), Image.LANCZOS))
            for key, path in self.resource_images.items()
        }
        self.num_imgs = {
            num: ImageTk.PhotoImage(Image.open(path).resize((50, 50), Image.LANCZOS))  # Adjust this as necessary
            for num, path in self.number_images.items()
        }

    def create_board(self):
        self.canvas = tk.Canvas(self.root, width=800, height=800, bg="white")
        self.canvas.pack()

        for row, tiles in enumerate(self.board.tile_grid):
            for col, tile in enumerate(tiles):
                pos = self.positions[row + 1][col]  # Get the specific position for each tile
                tile_img = self.tile_imgs.get(tile)
                if tile_img:
                    self.canvas.create_image(pos[0], pos[1], image=tile_img, anchor="nw")

                number = self.board.grid[row][col]
                if number != 7:
                    num_img = self.num_imgs.get(number)
                    if num_img:
                        self.canvas.create_image(
                            pos[0] + self.tile_size[0] / 2 - 25, pos[1] + self.tile_size[1] / 2 - 25,
                            image=num_img, anchor="nw"
                        )





# Create and display the board
board = Board()  # Assumes Board class has been initialized
CatanInterface(board)