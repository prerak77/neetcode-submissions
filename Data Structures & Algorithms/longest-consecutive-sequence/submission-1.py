class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # need to add everything in a set so that the search in o(1)
        num_set = set()
        for i in nums:
            num_set.add(i)

        
        main_counter = 0
        for i in nums:
            prev_num = i - 1
            if prev_num not in num_set:
                next_num = i
                inner_counter = 1
                while True:
                    next_num = next_num + 1
                    if next_num in num_set:
                        inner_counter += 1
                    else :
                        if inner_counter > main_counter :
                            main_counter = inner_counter
                        break

        return main_counter 




