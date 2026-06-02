class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        for i in range(0,len(temperatures)):
            res.append(0)

        for i in range(0,len(temperatures)):
            if stack == []:
                stack.append(0)
            else:
                print(res,stack)
                while temperatures[i] > temperatures[stack[-1]]:
                    largest_index = stack.pop()
                    res[largest_index] = i-largest_index
                    if stack == []:
                        break
                stack.append(i)

        return res 