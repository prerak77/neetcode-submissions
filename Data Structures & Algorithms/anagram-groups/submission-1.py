class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_data = {}
        for i in strs:
            inner_hash = {}
            for j in i:
                if j in inner_hash:
                    inner_hash[j] += 1
                else:
                    inner_hash[j] = 1
            inner_hash = tuple(sorted(inner_hash.items()))
            if inner_hash in hash_data:
                hash_data[inner_hash].append(i)
            else:
                hash_data[inner_hash] = [i]
        
        res = []
        for i in hash_data.values():
            res.append(i)
        return res
