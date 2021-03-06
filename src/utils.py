from random import choice

def generate_random_dice_values():
    return choice([1,2,3,4,5,6])

def next_player(current_player,current_config):
    if current_config != 6:
        if(current_player == "red"):
            return "green"
        elif(current_player == "green"):
            return "yellow"
        elif(current_player == "yellow"):
            return "blue"
        elif(current_player == "blue"):
            return "red"
        else:
            pass
    else:
        return current_player

def create_board_block(screen_position,color,position_x, position_y,block_method):
    block_parameters = 37
    relative_position_x = position_x
    relative_position_y = position_y
    if screen_position == "horizontal":
         for i in range(18):
            #rendering the red and yellow color blocks
            if (i==1 or i==7 or i==8 or i==9 or i==10 or i==11) and color == "red":
                block_method(True,color,relative_position_x, relative_position_y)
            elif (i==6 or i==7 or i==8 or i==9 or i==10 or i==16) and color == "yellow":
                block_method(True,color,relative_position_x, relative_position_y)
            else:
                block_method(False,color,relative_position_x,relative_position_y)
            relative_position_x += block_parameters #creates new block at new position
            #reset position at selected intervals
            if i == 5 or i==11: 
                relative_position_y += block_parameters
                relative_position_x = position_x
    elif screen_position == "vertical":
        for i in range(18):
            #rendering the blue and green color basics
            if (i==4 or i==6 or i==7 or i==8 or i==9 or i==10) and color=="blue":
                block_method(True,color,relative_position_x,relative_position_y)
            elif (i==7 or i==8 or i==9 or i==10 or i==11 or i==13) and color=="green":
                block_method(True,color,relative_position_x, relative_position_y)
            else:
                block_method(False,color,relative_position_x, relative_position_y)
            relative_position_y += block_parameters #creats new block at new position
            #reset position at selected image
            if i==5 or i==11:
                relative_position_x += block_parameters
                relative_position_y = position_y
    else:
        pass


def initial_positions():
    return{
        "1":[62,55],
        "2":[132,55],
        "3":[62,125],
        "4":[136,130]
        }

def find_blocks(index,positions):
   for element in positions:
       current_list = positions[element]
       if index+1 == int(element):
           return current_list

def update_game_piece(init_pos,piece_array,score):
    arr = [] 
    for piece in piece_array:
        if piece.is_on_game:
            arr.push(piece.number)
        if piece.is_on_game == False and score == 6:
           piece.rect = init_pos
           return
    choice = choice(arr)
    piece_array[choice].rect.x += score * 37 
