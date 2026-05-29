class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [len(temperatures) - 1]
        output = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack != [] and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                output.insert(0, stack[-1] - i)
            else:
                output.insert(0,0)
            stack.append(i)
            
        return output



