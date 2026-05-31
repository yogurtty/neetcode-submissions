class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pre = [0] * len(heights)
        post = [0] * len(heights)
        stack = []
        max = 0
        for i, num in enumerate(heights):
            while stack and num < heights[stack[-1]]:
                j = stack.pop()
                post[j] = (i - j) - 1
            stack.append(i)
        while stack:
            j = stack.pop()
            post[j] = len(heights) - j - 1
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                j = stack.pop()
                pre[j] = (j - i) - 1
            stack.append(i)
        while stack:
            j = stack.pop()
            pre[j] = j
        for i, num in enumerate(heights):
            sum = num+(num*pre[i])+(num*post[i])
            if sum > max:
                max = sum
        return max


        
