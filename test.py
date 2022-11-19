a = [

    [" "," "," "],
    ["B"," ","B"],
    [" "," "," "],
    [" "," "," "],
    ["S","S","S"]
]


def check_horizontal_matches(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == " ":
                continue
            else:
                curr_char = arr[i][j]
                curr_col = j
                while curr_col+1 < len(arr[0]):
                    next_col= curr_col+1
                    next_char = arr[i][next_col]
                    if next_char == curr_char:
                        print(curr_col)
                        #we have a match
                        print(next_char)
                        curr_col+=1
                    if curr_col+1 < len(arr[0]):
                        break
check_horizontal_matches(a)
