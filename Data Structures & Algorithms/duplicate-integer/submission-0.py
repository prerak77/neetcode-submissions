class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_Set = set()
        for i in nums:
            if i in hash_Set:
                return True
            hash_Set.add(i)
        return False