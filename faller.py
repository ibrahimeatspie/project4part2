from jewel import Jewel
from errors import *
class Faller:
    def __init__(self, top, mid, bot, board):
        self.top = top
        self.mid = mid
        self.bot = bot
        self.board = board
        if self.top.get_row() != 0 or self.mid.get_row() != 1 or self.bot.get_row() != 2:
            raise InvalidJewels("All jewels creating faller must have top row at 0, middle row at 1, and bottom row at 2")
    def get_top(self):
        return self.top

    def get_mid(self):
        return self.mid
    
    def get_bot(self):
        return self.bot

    def set_status_of_jewels(self, status):
        game_over = self.board.get_game_over_status()
        if game_over:
            raise GameOverError('You are attempting to set status after game is over')
        else:
            self.top.set_status(status)
            self.mid.set_status(status)
            self.bot.set_status(status)
    def freeze(self):
        game_over = self.board.get_game_over_status()
        if game_over:
            raise GameOverError('You are attempting to freeze board after game is over')
        else:
            self.top.set_status(" ")
            self.mid.set_status(" ")
            self.bot.set_status(" ")
            self.board.set_faller(None)



    def rotate(self):
        game_over = self.board.get_game_over_status()
        if game_over:
            raise GameOverError('You are attempting to rotate after game is over')
        else:
            status = self.bot.get_status()
            if status != " " and status!="*":
                old_top_color = self.top.get_color()
                old_mid_color = self.mid.get_color()
                old_bot_color = self.bot.get_color()

                self.top.set_color(old_bot_color)
                self.mid.set_color(old_top_color)
                self.bot.set_color(old_mid_color)

    


    def move_down(self):
        game_over = self.board.get_game_over_status()
        if game_over:
            raise GameOverError('You are attempting to move faller down after game is over')
        else:
            status = self.bot.get_status()
            bot_row, bot_col = self.bot.get_row(), self.bot.get_col()
            mid_row, mid_col = self.mid.get_row(), self.mid.get_col()
            top_row, top_col = self.top.get_row(), self.top.get_col()
            if status == "[":
                if bot_row+1 < len(self.board.arr):
                    #one row lower is within the board
                    if self.board.arr[bot_row+1][bot_col] == " ":
                        #the cell below is empty
                        self.top.set_row(self.top.get_row()+1)
                        self.mid.set_row(self.mid.get_row()+1)
                        self.bot.set_row(self.bot.get_row()+1)

                        #update the board to show the new position
                        self.board.arr[top_row][top_col] = " "
                        self.board.arr[bot_row][bot_col] = self.mid
                        self.board.arr[mid_row][mid_col] = self.top
                        self.board.arr[bot_row+1][bot_col] = self.bot
                        
                        new_bot_row = self.bot.get_row()
                        if new_bot_row == len(self.board.arr)-1 or self.board.arr[new_bot_row+1][bot_col] != " ":
                            self.set_status_of_jewels("|")
    
    def move_left(self):
        game_over = self.board.get_game_over_status()
        if game_over:
            raise GameOverError('You are attempting to move faller left after game is over')
        else:
            status = self.bot.get_status()
            bot_row, bot_col = self.bot.get_row(), self.bot.get_col()
            mid_row, mid_col = self.mid.get_row(), self.mid.get_col()
            top_row, top_col = self.top.get_row(), self.top.get_col()
            col = bot_col
            if status == "[" or status=="|":
                #print(bot_col-1)
                if bot_col-1 > -1:
                    #print("ASD")
                    #one col to left is within the board
                    if self.board.arr[bot_row][col-1] == " " and self.board.arr[mid_row][col-1] == " " and self.board.arr[top_row][col-1] == " ":
                        if status=="|":
                            self.set_status_of_jewels("[")
                        #the cell to left is empty
                        self.top.set_col(self.top.get_col()-1)
                        self.mid.set_col(self.mid.get_col()-1)
                        self.bot.set_col(self.bot.get_col()-1)

                        #update the board to show the new position
                        self.board.arr[bot_row][bot_col] = " "
                        self.board.arr[mid_row][mid_col] = " "
                        self.board.arr[top_row][top_col] = " "

                        self.board.arr[bot_row][col-1] = self.bot
                        self.board.arr[mid_row][col-1] = self.mid
                        self.board.arr[top_row][col-1] = self.top

                        new_col = col-1
                        
                        
                        if self.bot.get_row() == len(self.board.arr)-1 or self.board.arr[self.bot.get_row()+1][new_col] != " ":
                            self.set_status_of_jewels("|")

                    #update the arr 
    def move_right(self):
        game_over = self.board.get_game_over_status()
        if game_over:
            raise GameOverError('You are attempting to move faller right after game is over')
        else:
            status = self.bot.get_status()
            bot_row, bot_col = self.bot.get_row(), self.bot.get_col()
            mid_row, mid_col = self.mid.get_row(), self.mid.get_col()
            top_row, top_col = self.top.get_row(), self.top.get_col()
            col = bot_col
            if status == "[" or status == "|":
                #print(bot_col-1)
                if bot_col+1 < len(self.board.arr[0]):
                    #print("ASD")
                    #one col to right is within the board
                    if self.board.arr[bot_row][col+1] == " " and self.board.arr[mid_row][col+1] == " " and self.board.arr[top_row][col+1] == " ":
                        if status=="|":
                            self.set_status_of_jewels("[")
                        #the cell to the right is empty
                        self.top.set_col(self.top.get_col()+1)
                        self.mid.set_col(self.mid.get_col()+1)
                        self.bot.set_col(self.bot.get_col()+1)

                        #update the board to show the new position
                        self.board.arr[bot_row][bot_col] = " "
                        self.board.arr[mid_row][mid_col] = " "
                        self.board.arr[top_row][top_col] = " "

                        self.board.arr[bot_row][col+1] = self.bot
                        self.board.arr[mid_row][col+1] = self.mid
                        self.board.arr[top_row][col+1] = self.top
                        new_col = col+1
                        if self.bot.get_row() == len(self.board.arr)-1 or self.board.arr[self.bot.get_row()+1][new_col] != " ":
                            self.set_status_of_jewels("|")
                        
                        """new_bot_row = self.bot.get_row()
                        if new_bot_row == len(self.board.arr)-1 or self.board.arr[new_bot_row+1][bot_col] != " ":
                            self.set_status_of_jewels("|")"""

                    #update the arr 

        




