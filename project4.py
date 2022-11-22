from board import *

if __name__ == "__main__":
    rows = int(input())
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

                
                    
                    
                elif move[0] == "R":
                    #we are rotating
                    if board.faller != None:
                        board.faller.rotate()
                    print_board(board.arr)
                    if board.gameover == True:
                        game_over = True
                        print("GAME OVER")
                        break
                    
                elif move[0] == "<":
                    if board.faller != None:
                        board.faller.move_left()
                    print_board(board.arr)
                    if board.gameover == True:
                        #check game over for moving faller here
                        game_over = True
                        print("GAME OVER")
                        break

                elif move[0] == ">":
                    if board.faller != None:
                        board.faller.move_right()
                    print_board(board.arr)
                    if board.gameover == True:
                        game_over = True
                        print("GAME OVER")
                        break
                elif move[0] == "Q":
                    game_over = True
                    break
                else:
                    raise InvalidMoveError("Inputted move does not exist")
        
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
