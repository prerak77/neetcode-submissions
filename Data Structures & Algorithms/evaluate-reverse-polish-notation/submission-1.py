class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+","*","-","/"]:
                opr_2 = int(stack.pop())
                opr_1 = int(stack.pop())
                if i == "+":
                    stack.append(opr_1 + opr_2)
                elif i == "*":
                    stack.append(opr_1 * opr_2)
                elif i == "-":
                    stack.append(opr_1 - opr_2)
                elif i == "/":
                    stack.append(opr_1 / opr_2)
            else:
                stack.append(i)

        return int(stack.pop())

        