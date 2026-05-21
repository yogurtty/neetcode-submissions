class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {"(", "{", "["}
        
        for char in s:
            if char in open:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == chr(ord(stack[-1])+2):
                    stack.pop()
                elif char == chr(ord(stack[-1])+1):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        