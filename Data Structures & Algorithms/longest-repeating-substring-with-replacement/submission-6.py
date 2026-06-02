class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ele_in_window = {}
        max_freq = 0
        window_size = 0

        for right in range(len(s)):
            if s[right] in ele_in_window.keys():
                ele_in_window[s[right]] +=1
            else:
                ele_in_window[s[right]] =1
            
            max_freq = max(ele_in_window.values())
            while((right-left+1) - max_freq)>k:
                ele_in_window[s[left]]-=1
                left +=1
            window_size = max(window_size,right-left+1)
        return window_size