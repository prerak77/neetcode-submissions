class TimeMap:

    def __init__(self):
        
        self.hash_set = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_set.keys():
            inner_hash = self.hash_set[key]
            inner_hash[timestamp] = value
        else:
            inner_hash = {}
            inner_hash[timestamp] = value
            self.hash_set[key] = inner_hash


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_set:
            return ""
        inner_hash = self.hash_set[key]
        key_lst = list(inner_hash.keys())  # assume sorted

        left, right = 0, len(key_lst) - 1
        res = ""  # best candidate so far

        while left <= right:
            mid = (left + right) // 2
            if key_lst[mid] <= timestamp:
                res = inner_hash[key_lst[mid]]  # candidate
                left = mid + 1                  # try to find later timestamp
            else:
                right = mid - 1

        return res

        
