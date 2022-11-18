from faller import *
from general_funcs import *
from jewel import *


class Board:
    def __init__(self, arr, faller = None, matches = None):
        self.arr = arr
        self.faller = faller
        self.matches = matches
    def set_matches(self, matches):
        self.matches = matches
    def set_faller(self, faller):
        self.faller = faller
    def insert_faller(self, faller):
        if self.faller == None:
            self.faller = faller
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
        
        if self.faller.get_bot().get_status() == "[":
            self.faller.move_down()
        if self.faller.get_bot().get_status() == "|":
            self.faller.freeze()
        if self.faller == None:
            self.check_horizontal_matches()
           
            #check for matches
            #if there are matches, remove matches and then check for matches
            #fi there aren't matches, check for matches 
    def check_horizontal_matches(self):
        print("checking matches")
        matches = []
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                element = self.arr[i][j]
                
                if element != " ":
                    
                    #print(element.get_color())
                    matching_chars = []
                    color = element.get_color()
                    #print(i,j)
                    #matching_chars.append(color)
                    z = j+1
                    for z in range(len(self.arr[i])):

                        #print(self,arr[i][z])
                        if self.arr[i][z] == " ":
                            break
                        if self.arr[i][z].get_color() == color:
                            #print(element.get_color())
                            print(i,z)
                            matching_chars.append(self.arr[i][z].get_color())
                        else:
                            break
                    #print(matching_chars)
                    if len(matching_chars)>=3:
                        matches.append(matching_chars)
        print(matches)

            
a = [

    [" "," ","G"],
    [" "," "," "],
    [" "," ","Y"],
    [" "," "," "],
    ["S"," ","S"]
]

arr = create_predef_board(a)
b = Board(arr)
top = Jewel("Y", 0, 1, "[")
mid = Jewel("A", 1, 1, "[")
bot = Jewel("S", 2, 1, "[")
f = Faller(top, mid, bot, b)
b.insert_faller(f)
print_board(b.arr)
b.iterate()
print_board(b.arr)
b.iterate()
print_board(b.arr)
b.iterate()
print_board(b.arr)
b.iterate()
print_board(b.arr)
b.iterate()
print_board(b.arr)


