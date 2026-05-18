class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char.lower() for char in s if char.isalnum())
        for i, char in enumerate(clean):
            if char == clean[len(clean) - i - 1]:
                continue
            else:
                return False
        return True
        