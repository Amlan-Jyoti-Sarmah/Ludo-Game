import pygame 
from sys import exit
from Board import Board
from Board import Status_Board
from Block import Block
from Player import Player
from utils import create_board_block
from utils import find_blocks
from utils import generate_random_dice_values
from utils import next_player 
from utils import update_game_piece

pygame.init() #initialize pygame

# creating the window and basic global game variables
WIDTH = 547
HEIGHT = 600
IS_PLAYING = True
TURN = "red"
current_number = 6
font = pygame.font.SysFont('arial', 50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo")

#game imports
red_board = pygame.image.load('../assets/red_board.png').convert_alpha()
yellow_board = pygame.image.load('../assets/yellow_board.png').convert_alpha()
green_board = pygame.image.load('../assets/green_board.png').convert_alpha()
blue_board = pygame.image.load('../assets/blue_board.png').convert_alpha()
center_board = pygame.image.load('../assets/center_board.png').convert_alpha()
block_image = pygame.image.load('../assets/game_block.png').convert_alpha()
block_image_red = pygame.image.load('../assets/game_block_red.png').convert_alpha()
block_image_yellow = pygame.image.load('../assets/game_block_yellow.png').convert_alpha()
block_image_green = pygame.image.load('../assets/game_block_green.png').convert_alpha()
block_image_blue = pygame.image.load('../assets/game_block_blue.png').convert_alpha()
display_board = pygame.image.load('../assets/display_board.png').convert_alpha()
red_piece = pygame.image.load('../assets/red.png').convert_alpha()
yellow_piece = pygame.image.load('../assets/yellow.png').convert_alpha()
blue_piece = pygame.image.load('../assets/blue.png').convert_alpha()
green_piece = pygame.image.load('../assets/green.png').convert_alpha()

# creating board
board = pygame.sprite.Group()
board.add(Board('Red',red_board))
board.add(Board('Green',green_board))
board.add(Board('Blue',blue_board))
board.add(Board('Yellow',yellow_board))
board.add(Board('Center',center_board))

#getting inital position for board pieces
board_group_sprites = board.sprites()
red_piece_initial_pos = board_group_sprites[0].initial_index_per_color()
green_piece_initial_pos = board_group_sprites[1].initial_index_per_color()
blue_piece_initial_pos = board_group_sprites[2].initial_index_per_color()
yellow_piece_initial_pos = board_group_sprites[3].initial_index_per_color()

# blocks and status board
block = pygame.sprite.Group()
status_board = pygame.sprite.Group()
status_board.add(Status_Board(display_board))

#rendering block on board this goes as the block method for create_board_block funtion that performs the calculations and creates the blocks for the board
def render_blocks(is_special,color,position_x,position_y):
    if is_special:
        if color == "red":
            block.add(Block(block_image_red,position_x,position_y))
        elif color == "yellow":
            block.add(Block(block_image_yellow,position_x,position_y))
        elif color == "blue":
            block.add(Block(block_image_blue,position_x,position_y))
        elif color == "green":
            block.add(Block(block_image_green,position_x,position_y))
        else:
            pass
    else:
        block.add(Block(block_image,position_x,position_y))

#Pieces configuration
red_piece_group = pygame.sprite.Group()
yellow_piece_group = pygame.sprite.Group()
blue_piece_group = pygame.sprite.Group()
green_piece_group = pygame.sprite.Group()

def render_initial_players(color):
    if color == "red":
        for i in range(4):
            positions = find_blocks(i,red_piece_initial_pos)
            red_piece_group.add(Player(color,red_piece,positions[0],positions[1],False,i+1))
    elif color == "yellow":
        for i in range(4):
            positions = find_blocks(i,yellow_piece_initial_pos)
            yellow_piece_group.add(Player(color,yellow_piece,positions[0],positions[1],False,i+1))
    elif color == "green":
        for i in range(4):
            positions = find_blocks(i,green_piece_initial_pos)
            green_piece_group.add(Player(color,green_piece,positions[0],positions[1],False,i+1))
    elif color == "blue":
        for i in range(4):
            positions = find_blocks(i,blue_piece_initial_pos)
            blue_piece_group.add(Player(color,blue_piece,positions[0],positions[1],False,i+1))
    else:
        pass

render_initial_players("red")
render_initial_players("yellow")
render_initial_players("blue")
render_initial_players("green")

#display current score/number
def display_score(score,font):
    surface = font.render(f"{score}",False,(64,64,64))
    rect = surface.get_rect(topright=(470,550))
    screen.blit(surface,rect)

print(red_piece_initial_pos)

#update game
def update_game():
    if TURN == "red":
        update_game_piece(red_piece_initial_pos[0],red_piece_group,current_number)
    elif TURN == "yellow":
        update_game_piece()
    elif TURN == "green":
        update_game_piece()
    elif TURN == "blue":
        update_game_piece()
    else:
        pass

#clock and FPS
clock = pygame.time.Clock()

#game loop
create_board_block("horizontal","red",0,214,render_blocks)
create_board_block("horizontal","yellow",325,214,render_blocks)
create_board_block("vertical","green",217,0,render_blocks)
create_board_block("vertical","blue",217,325,render_blocks)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            current_number = generate_random_dice_values()
            TURN = next_player(TURN,current_number)
    screen.fill('White')
    #Drawing board and block
    board.draw(screen) 
    block.draw(screen)
    status_board.draw(screen)
    red_piece_group.draw(screen)
    yellow_piece_group.draw(screen)
    blue_piece_group.draw(screen)
    green_piece_group.draw(screen)
    display_score(current_number,font)
    pygame.display.update()
    clock.tick(60)
