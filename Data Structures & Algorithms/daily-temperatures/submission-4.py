class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                j = stack.pop()
                output[j] = (i - j)
            stack.append(i)
        return output


            
            
        