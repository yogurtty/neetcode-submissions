class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        left = height[i]
        right = height[j]
        sum = 0
        while i < j:
            if left < right:
                i += 1
                if height[i] < left:
                    sum += left-height[i]
                else:
                    left = height[i]
            else:
                j -= 1
                if height[j] < right:
                    sum += right-height[j]
                else:
                    right = height[j]
        return sum

        