class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        #rules out no rotations
        if nums[left] < nums[right]:
            return nums[left]
        left = 1

        mid = int((left+right)/2)
        
        while (left <= right):
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[0] < nums[mid]:
                left = mid + 1
            else: 
                right = mid - 1 
            mid = int((left+right)/2)
        return nums[mid]
        