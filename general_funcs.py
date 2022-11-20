from jewel import Jewel


status_dict = {"[": "]", "|": "|", "*": "*", " ": " "}


def create_size_arr(rows, cols):
    arr = []
    for i in range(3):
        arr.append([])
        for j in range(cols):
            arr[i].append(' ')
            
    for i in range(3, rows+3):
        arr.append([])
        for j in range(cols):
            arr[i].append(" ")
    return arr


def print_board(arr):
        
    for i in range(3, len(arr)):
        print("|", end="")
        for j in range(len(arr[i])):
            curr_element = arr[i][j]
            if curr_element == " ":
                print(" ", end="")
                print(" ", end="")
                print(" ", end="")
            else:
                jewel = curr_element
                print(jewel.get_status(), end="")
                print(jewel.get_color(), end="")
                print(status_dict[jewel.get_status()], end="")
                
        print("|", end="")
        print()
    print(" ",end="")
    for i in range(3*len(arr[0])):
        print("-", end="")
    print(" ",end="")
    print()


def create_predef_board(arr):

    new_arr = []
    for i in range(3):
        new_arr.append([])
        for j in range(len(arr[0])):
            new_arr[i].append(" ")

    for c in range(len(arr[0])):
        stack = []
        for r in range(len(arr)-1, -1, -1):
            if arr[r][c] != " ":
                stack.append(arr[r][c])
                arr[r][c] = " "
        stack = stack[::-1]
        for i in range(len(arr)-1, -1, -1):
            if len(stack)>0:
                arr[i][c] = stack.pop()

    for i in range(0, len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != " ":
                arr[i][j] = Jewel(arr[i][j], i, j, " ")

    for row in arr:
        new_arr.append(row)       
    
    return new_arr




def get_rid_of_matches_in_board(board):
    arr = board.arr
    
    for i in range(3, len(board.arr)):
        for j in range(len(board.arr[i])):
            if board.arr[i][j] == " ":
                continue
            else:
                if board.arr[i][j].get_status() == "*":
                    board.arr[i][j] = " "
                    

    for c in range(len(board.arr[0])):
        stack = []
        for r in range(len(board.arr)-1, -1, -1):
            if board.arr[r][c] != " ":
                stack.append(board.arr[r][c])
                board.arr[r][c] = " "
        stack = stack[::-1]
        
        for i in range(len(board.arr)-1, -1, -1):
            if len(stack)>0:
                board.arr[i][c] = stack.pop()
 
    return board.arr

 