from faller import *
from general_funcs import *
from jewel import *
from errors import*

class Board:
    def __init__(self, arr, faller = None):
        self.arr = arr
        self.faller = faller
        self.gameover = False
        self.check_vertical_matches()
        self.check_horizontal_matches()
        self.check_diagonal_up_matches()
        self.check_diagonal_down_matches()
        
    def get_game_over_status(self):
        return self.gameover
    def set_faller(self, faller):
        if self.gameover:
            raise GameOverError("Game is over")
        else:
        
            self.faller = faller
    def insert_faller(self, faller):
        if self.gameover:
            raise GameOverError("Cannot insert faller after game is over")
        else:
            if self.faller == None:
                self.faller = faller
                if self.faller.get_bot().get_col() >= len(self.arr[0]) or self.faller.get_bot().get_col() < 0:
                    raise InvalidFallerInsertion("Cannot insert faller in non existing column")
        
                else:
                    self.faller.move_down()
                    top = self.faller.get_top()
                    top_row, top_col = top.get_row(), top.get_col()
                    mid = self.faller.get_mid()
                    mid_row, mid_col = mid.get_row(), mid.get_col()
                    bot = self.faller.get_bot()
                    bot_row, bot_col = bot.get_row(), bot.get_col()
                    self.arr[bot_row][bot_col] = bot
                    self.arr[mid_row][mid_col] = mid
                    self.arr[top_row][top_col] = top
    def iterate(self):
        if self.gameover:
            raise GameOverError("Cannot iterate, game is over")
        else:
        #print_board(self.arr)
            if self.faller == None:
                #print("we have matches")
                
                new_arr = get_rid_of_matches_in_board(self)
                self.arr = new_arr
                self.check_vertical_matches()
                self.check_horizontal_matches()
                self.check_diagonal_up_matches()
                self.check_diagonal_down_matches()
                #print_board(new_arr)
                #print(get_rid_of_spaces_in_board(self.arr))
                #self.remove_matches()
            else:
                if self.faller.get_bot().get_status() == "[":
                    self.faller.move_down()
                elif self.faller.get_bot().get_status() == "|":
                    self.faller.freeze()
                    #pass
                if self.faller == None:
                    vertical_match = self.check_vertical_matches()
                    horizontal_match = self.check_horizontal_matches()
                    diagonal_up_match = self.check_diagonal_up_matches()
                    diagonal_down_match = self.check_diagonal_down_matches()

                    if vertical_match == False and horizontal_match == False and diagonal_down_match== False  and diagonal_up_match== False and self.has_hidden_jewels():
                        self.gameover = True
                        #print("no matches, game over") 
                #check for matches
                #if there are matches, remove matches and then check for matches
                #fi there aren't matches, check for matches 
        
            #self.arr = create_predef_board(self.arr)
            #arr = create_predef_board(self.arr)
        
    def check_horizontal_matches(self):
        if self.gameover:
            raise GameOverError("cannot check horizontal matches after game is over")
        else:
            has_match = False
            arr = self.arr
            all_matches = []
            
            for i in range(3, len(arr)):
            
                matches_set = set()
                matches_arr = []
                for j in range(len(arr[i])-2):
                    
                    left_cell = arr[i][j]
                    mid_cell = arr[i][j+1]
                    right_cell = arr[i][j+2]

                    if left_cell == " " or mid_cell == " " or right_cell == " ":
                        continue
                        
                    else:
                            if left_cell.get_color() == mid_cell.get_color() and mid_cell.get_color() == right_cell.get_color():
                                has_match = True
                                if left_cell not in matches_set:
                                    left_cell.set_status("*")
                                    matches_set.add(left_cell)
                                    matches_arr.append(left_cell)
                                if mid_cell not in matches_set:
                                    mid_cell.set_status("*")
                                    matches_set.add(mid_cell)
                                    matches_arr.append(mid_cell)
                                if right_cell not in matches_set:
                                    right_cell.set_status("*")
                                    matches_set.add(right_cell)
                                    matches_arr.append(right_cell)
                                
                            else:
                                continue
            return has_match   
    
    def check_vertical_matches(self):
        if self.gameover:
            raise GameOverError("Cannot check for vertical matches after game is over")
        else:
            has_match = False
            arr = self.arr
            all_matches = []
            
            for col in range(len(arr[0])):

                matches_set = set()
                matches_arr = []

                for row in range(len(arr)-2):

                    top_cell = arr[row][col]
                    mid_cell = arr[row+1][col]
                    bot_cell = arr[row+2][col]

                    if top_cell == " " or mid_cell == " " or bot_cell == " ":
                        continue
                    else:
                        #print(top_cell.get_color(), mid_cell.get_color(), bot_cell.get_color())
                        if top_cell.get_color() == mid_cell.get_color() and mid_cell.get_color() == bot_cell.get_color():
                                has_match = True
                                if top_cell not in matches_set:
                                    top_cell.set_status("*")
                                    matches_set.add(top_cell)
                                    matches_arr.append(top_cell)
                                if mid_cell not in matches_set:
                                    mid_cell.set_status("*")
                                    matches_set.add(mid_cell)
                                    matches_arr.append(mid_cell)
                                if bot_cell not in matches_set:
                                    bot_cell.set_status("*")
                                    matches_set.add(bot_cell)
                                    matches_arr.append(bot_cell)
                                
                        else:
                            continue
                if len(matches_arr) > 0:
                    all_matches.append(matches_arr)
            #print(all_matches)
            return has_match   

    def check_diagonal_up_matches(self):
        if self.gameover:
            raise GameOverError("cannot check diagonal up matches after game is over")
        else:
            has_match = False
            arr = self.arr
            all_matches = []
            matches_set = set()
            

            for col in range(len(arr[0])-2):

                for row in range(len(arr)-1, 3, -1):
                    bot_left = arr[row][col]
                    mid = arr[row-1][col+1]
                    top_right = arr[row-2][col+2]
                    if bot_left == " " or mid == " " or top_right == " ":
                        continue
                    else:
                        if bot_left.get_color()==mid.get_color() and mid.get_color()==top_right.get_color():
                            has_match = True
                            if bot_left not in matches_set:
                                bot_left.set_status("*")
                                matches_set.add(bot_left)
                            if mid not in matches_set:
                                mid.set_status("*")
                                matches_set.add(mid)
                            if top_right not in matches_set:
                                top_right.set_status("*")

                                matches_set.add(bot_left)
                        else:
                            continue
                """for jewel in matches_set:
                    row = jewel.get_row()
                    col = jewel.get_col()
                    print((row, col),jewel.get_color())"""
            return has_match

    def check_diagonal_down_matches(self):
        if self.gameover:
            raise GameOverError("cannot check diagonal down matches after game is over")
        else:
            has_match = False
            arr = self.arr
            all_matches = []
            matches_set = set()
            

            for col in range(len(arr[0])-2):

                for row in range(2, len(arr)-2, 1):

                    top_left = arr[row][col]
                    mid = arr[row+1][col+1]
                    bot_right = arr[row+2][col+2]


                    
                    if top_left == " " or mid == " " or bot_right == " ":
                        continue
                    else:
                        if top_left.get_color()==mid.get_color() and mid.get_color()==bot_right.get_color():
                            has_match = True
                            if top_left not in matches_set:
                                top_left.set_status("*")
                                matches_set.add(top_left)
                            if mid not in matches_set:
                                mid.set_status("*")
                                matches_set.add(mid)
                            if bot_right not in matches_set:
                                bot_right.set_status("*")

                                matches_set.add(bot_right)
                        else:
                            continue
                """for jewel in matches_set:
                    row = jewel.get_row()
                    col = jewel.get_col()
                    print((row, col),jewel.get_color())"""
            return has_match
    def has_hidden_jewels(self):
        if self.gameover:
            raise GameOverError("Cannot check for hidden jewels after game is over")
        else:
            arr = self.arr
            for i in range(0,3):
                for j in range(len(arr[0])):
                    if arr[i][j] != " ":
                        return True
            return False
            



"""rows = int(input())
cols = int(input())
empty_or_contents = input()
if empty_or_contents == "EMPTY":
    arr = create_size_arr(rows, cols)
    board = Board(arr)
    print_board(board.arr)

    game_over = False
    while not game_over:
        move = input()
        if move == '':
            board.iterate()
            print_board(board.arr)
            if board.gameover == True:
                game_over = True
                print("GAME OVER")
                break

        else:
            if move[0] == "F":
            #we are inserting a faller
                faller_column = int(move[2])-1

                top_color = move[4]
                mid_color = move[6]
                bot_color = move[8]

                #color, row, col, status
                top_jewel = Jewel(top_color, 0, faller_column, "[")
                mid_jewel = Jewel(mid_color, 1, faller_column, "[")
                bot_jewel = Jewel(bot_color, 2, faller_column, "[")

                faller = Faller(top_jewel, mid_jewel, bot_jewel, board)

                cell_below = board.arr[3][faller_column]
                if cell_below != " ":
                    board.gameover = True
                    print("GAME OVER")
                    game_over = True
                    break
                else:
                    board.insert_faller(faller)

                    print_board(board.arr)

              
                
                
            if move[0] == "R":
                #we are rotating
                if board.faller != None:
                    board.faller.rotate()
                print_board(board.arr)
                if board.gameover == True:
                    game_over = True
                    print("GAME OVER")
                    break
                
            if move[0] == "<":
                if board.faller != None:
                    board.faller.move_left()
                print_board(board.arr)
                if board.gameover == True:
                    game_over = True
                    print("GAME OVER")
                    break

            if move[0] == ">":
                if board.faller != None:
                    board.faller.move_right()
                print_board(board.arr)
                if board.gameover == True:
                    game_over = True
                    print("GAME OVER")
                    break
            if move[0] == "Q":
                game_over = True
                break
    
elif empty_or_contents == "CONTENTS":
    arr = []
    for i in range(rows):
        curr_row_input = input()
        arr_version_of_input = [*curr_row_input]
        arr.append(arr_version_of_input)

    arr = create_predef_board(arr)
    board = Board(arr)
    print_board(board.arr)

    game_over = False
    while not game_over:
        move = input()
        if move == '':
            board.iterate()
            print_board(board.arr)
            if board.gameover == True:
                game_over = True
                print("GAME OVER")
                break

        else:
            if move[0] == "F":
            #we are inserting a faller
                faller_column = int(move[2])-1

                top_color = move[4]
                mid_color = move[6]
                bot_color = move[8]

                #color, row, col, status
                top_jewel = Jewel(top_color, 0, faller_column, "[")
                mid_jewel = Jewel(mid_color, 1, faller_column, "[")
                bot_jewel = Jewel(bot_color, 2, faller_column, "[")

                faller = Faller(top_jewel, mid_jewel, bot_jewel, board)

                cell_below = board.arr[3][faller_column]
                if cell_below != " ":
                    board.gameover = True
                    print("GAME OVER")
                    game_over = True
                    break
                else:
                    board.insert_faller(faller)

                    print_board(board.arr)

              
                
                
            if move[0] == "R":
                #we are rotating
                if board.faller != None:
                    board.faller.rotate()
                print_board(board.arr)
                if board.gameover == True:
                    game_over = True
                    print("GAME OVER")
                    break
                
            if move[0] == "<":
                if board.faller != None:
                    board.faller.move_left()
                print_board(board.arr)
                if board.gameover == True:
                    game_over = True
                    print("GAME OVER")
                    break

            if move[0] == ">":
                if board.faller != None:
                    board.faller.move_right()
                print_board(board.arr)
                if board.gameover == True:
                    game_over = True
                    print("GAME OVER")
                    break
            if move[0] == "Q":
                game_over = True
                break
"""
    #board = Board(arr)"""


"""arr = [
    [" "," "," "],
    [" "," "," "],
    [" ","A"," "],
    [" ","B"," "]
]

a = create_predef_board(arr)
b = Board(a)
print_board(b.arr)
top_jewel = Jewel("B",0,1,"[")
mid_jewel = Jewel("A",1,1,"[")
bot_jewel = Jewel("A",2,1,"[")
faller = Faller(top_jewel,mid_jewel,bot_jewel,b)
b.insert_faller(faller)
print_board(b.arr)
b.iterate()
print_board(b.arr)
b.iterate()
print_board(b.arr)
b.iterate()
print_board(b.arr)"""











