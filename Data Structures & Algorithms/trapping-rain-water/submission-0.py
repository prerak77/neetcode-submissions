class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = right_max = total_water = 0
        head_ptr = 0
        tail_ptr = len(height)-1
        while head_ptr <= tail_ptr : 
            # the current height is the min value out of the 2 ptrs 
            current_height = height[head_ptr] if height[head_ptr] < height[tail_ptr] else height[tail_ptr]
          
            # the left max and rigt max are tallest walls on each side 
            left_max = height[head_ptr] if height[head_ptr] > left_max else left_max
            right_max = height[tail_ptr] if height[tail_ptr] > right_max else right_max

            # the water stored at a current position is teh min of the 2 walls minus the 
            # walls at the current position  
            curr_water_height = min(left_max,right_max)- current_height

            #only update the total water if there is postive water
            if curr_water_height > 0:
                total_water += curr_water_height

            # next we need to moves the pointers based on which values is smaller
            if height[head_ptr] < height[tail_ptr] :
                head_ptr += 1
            else :
                tail_ptr -=1
        return total_water
            


            





        