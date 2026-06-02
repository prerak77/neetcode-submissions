class Solution:
    def maxArea(self, heights: List[int]) -> int:
        breadth = len(heights)
        head = 0
        tail = len(heights)-1
        area = 0 
        while head < tail:
            height = min(heights[head],heights[tail])
            breadth = breadth - 1
            temp_area = height * breadth 
            if temp_area > area :
                area = temp_area
            if heights[head] > heights[tail]:
                tail -=1
            else :
                head +=1
        return area
