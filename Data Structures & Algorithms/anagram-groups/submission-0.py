class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_hash = {}
        for i in strs:
            inner_hash = {}
            for j in i:
                if j in inner_hash.keys():
                    inner_hash[j] +=1
                else:
                    inner_hash[j] = 1
            inner_hash = tuple(sorted(inner_hash.items()))
            if inner_hash in group_hash.keys():
                group_hash[inner_hash].append(i)
            else:
                group_hash[inner_hash] = [i]
        res = []
        for i in group_hash.keys():
            res.append(group_hash[i])
        return res
                