class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping_dic = {"}":"{","]":"[",")":"("}
        for i in s:
            if i in mapping_dic.keys():
                if len(stack) ==0:
                    return False

                if stack.pop() != mapping_dic[i]:
                    return False
            else:
                stack.append(i)
                
        if len(stack) !=0:
            return False 
        return True