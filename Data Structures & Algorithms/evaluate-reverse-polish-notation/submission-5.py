class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = []
        oper = {'+', "-", "*", "/"}
        for s in tokens:
            if s in oper:
                second = int(stack.pop())
                first = int(stack.pop())
                if s == "+":
                    stack.append(first + second)
                elif s == "-":
                    stack.append(first - second)
                elif s == "*":
                    stack.append(first * second)
                else:
                    result = first // second
                    if result < 0:
                        result = -1 * first // second
                        result *= -1
                    stack.append(result)         
            else:
                stack.append(s)
        return int(stack.pop())
