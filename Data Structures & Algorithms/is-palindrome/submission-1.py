class Solution:
    def isPalindrome(self, s: str) -> bool:
        # need 2 pointers one at the start and one at the end 
        head_pointer = 0
        tail_pointer = len(s)-1

        # need to loop through the string using 2 pointers till
        # the 2 pointers meet cross each other 
        while head_pointer <= tail_pointer :
            
            if (s[head_pointer].isalnum() == False):
                head_pointer +=1
                continue
            if (s[tail_pointer].isalnum() == False):
                tail_pointer -=1
                continue
            if (s[head_pointer].lower() != s[tail_pointer].lower()):
                return False
            else:
                head_pointer +=1
                tail_pointer -=1
        return True



        