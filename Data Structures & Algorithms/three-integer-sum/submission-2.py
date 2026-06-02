class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(sorted_nums)):
            for j in range(i+1,len(sorted_nums)):
                curr_sum = sorted_nums[i]+sorted_nums[j]
                need_val = 0-curr_sum
                if need_val in sorted_nums[j+1:]:
                    satisfied_val = [sorted_nums[i],sorted_nums[j],need_val]
                    if satisfied_val not in res:
                        res.append(satisfied_val)

        return res
