class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = dict()
        for char in s1:
            freq[char] = freq.get(char, 0) + 1
        l = 0
        r = 0
        match = dict()
        for char in s2:
            r += 1
            if freq.get(char) is None:
                l = r
                match = dict()
                continue
            else:
                match[char] = match.get(char, 0) + 1
                while match.get(char, 0) > freq.get(char):
                    match[s2[l]] -= 1
                    l += 1 
                
            if match == freq:
                return True   
        return False 
        