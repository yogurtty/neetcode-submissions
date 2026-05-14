class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for char in s:
            if char in d:
                d[char] = d.get(char) + 1
            else:
                d[char] = 1
        for char in t:
            if char in d:
                d[char] = d.get(char) - 1
                if (d.get(char) == 0):
                    d.pop(char)
            else:
                return False
            

        return True
            

        