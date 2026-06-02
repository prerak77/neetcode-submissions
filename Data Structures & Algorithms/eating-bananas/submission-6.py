class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k is the rate at which u eat bananas per hr
        import math
        low = 1
        high = max(piles)
        res = 0
        
        while low <= high :
            mid = (low+high)//2

            total_time = 0
            for i in piles :
                total_time += math.ceil(i/mid)
            if total_time <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
                

            

