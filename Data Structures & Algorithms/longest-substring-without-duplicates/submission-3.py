class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        left = -1
        right = 0
        nax = 1
        for i, char in enumerate(s):
            right = i
            while s[right] in seen:
                left += 1
                if s[left] == s[right]:
                    break
                else:
                    if s[left] in seen:
                        seen.remove(s[left])
            if (right - left) > nax:
                nax = right - left 
            seen.add(char)
        return nax



        