class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        middle_lst = len(matrix)//2
        middle_ele = len(matrix[middle_lst])//2
        while True:
            if matrix[middle_lst][middle_ele] == target:
                return True 
            elif matrix[middle_lst][middle_ele] > target:
                while middle_lst >= 0:
                    if matrix[middle_lst][middle_ele] == target:
                        return True 
                    else:
                        if matrix[middle_lst][middle_ele] < target:
                            return False
                        elif middle_ele < 0:
                            middle_lst -=1
                            middle_ele = len(matrix[middle_ele])-1
                        else:
                            middle_ele -=1
                return False
            else:
                while middle_lst <= len(matrix)-1:
                    if matrix[middle_lst][middle_ele] == target:
                        return True 
                    else:
                        if matrix[middle_lst][middle_ele] > target:
                            return False
                        elif middle_ele >= len(matrix[middle_lst])-1:
                            middle_lst +=1
                            middle_ele = 0
                        else:
                            middle_ele +=1
                return False
            

            