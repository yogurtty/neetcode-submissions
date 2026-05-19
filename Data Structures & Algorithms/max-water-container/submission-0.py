class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ma = 0
        left = 0
        right = len(heights)-1
        amount = 0
        for i in range(0, len(heights)):

            if heights[left] > heights[right]:
                amount = heights[right] * (right - left)
            else:
                amount = heights[left] * (right - left)
            
            if amount > ma:
                ma = amount;
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return ma

        