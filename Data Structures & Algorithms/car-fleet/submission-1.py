class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # make a dic to map the cars start pos and speed
        dic = {}
        for i in range(0,len(position)):
            dic[position[i]] = speed[i]

        # next sort the keys
        sorted_dict = {k: dic[k] for k in sorted(dic.keys(), reverse=True)}

        # next we need a dic to store the time take by each car
        time_dic = {}
        for i in sorted_dict.keys():
            time_dic[i] = (target-i)/sorted_dict[i]
        
        # next we need a stack to keep track of the 
        # slowest groups 
        stack = []

        # next we loop through all the cars 
        # to get the slowest groups 
        print(dic)
        for i in time_dic.keys():
            if stack == []:
                stack.append(time_dic[i])
            else:
                if time_dic[i] > stack[-1]:
                    stack.append(time_dic[i])

        return len(stack)                    

