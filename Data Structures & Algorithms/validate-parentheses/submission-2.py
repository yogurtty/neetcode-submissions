class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")" : "(", "}" : "{", "]" : "["} 
        
        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        