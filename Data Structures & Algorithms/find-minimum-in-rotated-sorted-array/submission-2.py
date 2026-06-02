class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        mid = (left + right)//2
        while left != right != mid:
            if nums[left] > nums[right] :
                left+=1
                mid = (left + right)//2
            else :
                right -=1
                mid = (left + right)//2
        return nums[mid]