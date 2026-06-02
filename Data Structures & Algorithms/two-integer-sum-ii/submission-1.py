class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(numbers) -1
        while l_ptr <= r_ptr :
            curr_sum = numbers[l_ptr] + numbers[r_ptr]
            if curr_sum > target :
                r_ptr -=1
            elif curr_sum < target:
                l_ptr +=1
            else:
                return[l_ptr+1,r_ptr+1]