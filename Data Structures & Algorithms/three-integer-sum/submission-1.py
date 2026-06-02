class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #  need to first sort the given array in des order
        nums.sort()
        sorted_arr = nums
        final_arr = []
        print(nums)
        for i in range(len(sorted_arr)-1):
            head_pointer = i+1
            tail_pointer = len(sorted_arr)-1

            if i > 0 and sorted_arr[i] == sorted_arr[i-1]:
                continue
            
            while head_pointer < tail_pointer :
                if sorted_arr[i] + sorted_arr[head_pointer] + sorted_arr[tail_pointer] > 0:
                    tail_pointer -=1 
                elif sorted_arr[i] + sorted_arr[head_pointer] + sorted_arr[tail_pointer] < 0:
                    head_pointer +=1
                else:
                    final_arr.append([sorted_arr[i],sorted_arr[head_pointer],sorted_arr[tail_pointer]])

                    # need to skip duplictes 
                    # for head_pointer
                    while head_pointer < tail_pointer and sorted_arr[head_pointer] == sorted_arr[head_pointer+1]:
                        head_pointer+=1
                    # for tail_poiner
                    while head_pointer < tail_pointer and sorted_arr[tail_pointer] == sorted_arr[tail_pointer -1]:
                        tail_pointer -=1

                    head_pointer +=1 
                    tail_pointer -=1 
        return final_arr


