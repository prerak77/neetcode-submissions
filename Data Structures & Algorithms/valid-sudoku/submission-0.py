class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute forcing it is by looping thorugh each loop 
        # and then adding each new number to a set
        
        for i in range(9):
            row_seen = set()
            for j in range(9):
                if board[i][j].isdigit()==False:
                    continue
                if int(board[i][j]) in row_seen:
                    print('here')
                    return False
                else:
                    row_seen.add(int(board[i][j]))

        # now we need to make sure each column has no duplicates
        #  i can have a set for each column
        lst_col_set = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if (board[i][j].isdigit()==False):
                    continue
                if int(board[i][j]) in lst_col_set[j]:
                    print("here2")
                    return False
                else:
                    lst_col_set[j].add(int(board[i][j]))
        
        #now we need to check each individual boxes
        lst_box_set = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                    if (board[i][j].isdigit()==False):
                        continue
                    if i>5 :
                        if j > 5:
                            if int(board[i][j]) in lst_box_set[8]:
                                print("here3")
                                return False
                            else:
                                lst_box_set[8].add(int(board[i][j]))
                        elif j > 2:
                            if int(board[i][j]) in lst_box_set[7]:
                                print("here4")
                                return False
                            else:
                                lst_box_set[7].add(int(board[i][j]))
                        else:
                            if int(board[i][j]) in lst_box_set[6]:
                                print("here5")
                                return False
                            else:
                                lst_box_set[6].add(int(board[i][j]))
                    elif i>2 :
                        if j > 5:
                            if int(board[i][j]) in lst_box_set[5]:
                                print("here5")
                                return False
                            else:
                                lst_box_set[5].add(int(board[i][j]))
                        elif j > 2:
                            if int(board[i][j]) in lst_box_set[4]:
                                print(i,j)
                                print(board[i][j])
                                print(lst_box_set[4])
                                print("here7")
                                return False
                            else:
                                lst_box_set[4].add(int(board[i][j]))
                        else:
                            if int(board[i][j]) in lst_box_set[3]:
                                print("here8")
                                return False
                            else:
                                lst_box_set[3].add(int(board[i][j]))
                    else :
                        if j > 5:
                            if int(board[i][j]) in lst_box_set[2]:
                                print("here9")
                                return False
                            else:
                                lst_box_set[2].add(int(board[i][j]))
                        elif j > 2:
                            if int(board[i][j]) in lst_box_set[1]:
                                
                                print("here10")
                                return False
                            else:
                                lst_box_set[1].add(int(board[i][j]))
                        else:
                            if int(board[i][j]) in lst_box_set[0]:
                                print(board[i][j])
                                print(lst_box_set[0])
                                return False

                            else:
                                lst_box_set[0].add(int(board[i][j]))
        return True




        