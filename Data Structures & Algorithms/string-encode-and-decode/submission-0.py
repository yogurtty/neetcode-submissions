class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for stri in strs:
            for char in stri:
                string += chr(ord(char) + 1)
            string += "|"
        return string



    def decode(self, s: str) -> List[str]:
        string = [""]
        i = 0
        for char in s:
            if char == "|":
                string.append("")
            else:
                string[-1] += (chr(ord(char) - 1))
        string.pop()
        return string

