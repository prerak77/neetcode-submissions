class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ptr1 = 0
        ptr2 = 1
        max_profit =0
        while ptr2 < len(prices):
            curr_proft = 0
            if(prices[ptr1] > prices[ptr2]):
                ptr1 = ptr2
                ptr2 +=1
            else :
                curr_profit = prices[ptr2] - prices[ptr1]
                if (curr_profit > max_profit):
                    max_profit = curr_profit
                ptr2+=1
        return max_profit

