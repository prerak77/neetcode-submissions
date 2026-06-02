class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # start  the pointer in the middle
        pointer = len(nums)//2

        while True:
            if nums[pointer] == target :
                return pointer
            elif nums[pointer] > target:
                while pointer >= 0:
                    if nums[pointer] == target :
                        return pointer
                    else:
                        pointer-=1
                return -1
            else:
                while pointer <= len(nums)-1:
                    if nums[pointer] == target :
                        return pointer
                    else:
                        pointer+=1
                return -1

            


