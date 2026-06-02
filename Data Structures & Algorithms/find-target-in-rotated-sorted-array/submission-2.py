class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)-1
        left = 0
        mid = (right+left)//2
        while True :
            print(mid,right,left)
            if(nums[mid] == target ):
                return mid
            elif(right == mid == left):
                return -1 
            elif(nums[left] <= nums[mid]):
                if(target <= nums[mid] and target >=nums[left] ):
                    right = mid -1
                    mid = (right+left)//2
                else :
                    left = mid +1
                    mid = (right+left)//2
            else :
                if(target >= nums[mid] and target <=nums[right] ):
                    left  = mid +1
                    mid = (right+left)//2
                else :
                    right = mid -1
                    mid = (right+left)//2
