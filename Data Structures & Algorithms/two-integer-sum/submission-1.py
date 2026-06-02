class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_hash = {}
        for i in range(len(nums)):
            pos_hash[nums[i]] = i
        for i in range(len(nums)) :
            need = target - nums[i]
            if need in pos_hash.keys() and pos_hash[need]!=i:
                return [i,pos_hash[need]]