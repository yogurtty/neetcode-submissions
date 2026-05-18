class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        product = 1
        for i, num in enumerate(nums):
            prefix[i] = product
            product *= num
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        for i in range(0, len(nums)):
            nums[i] = prefix[i] * suffix[i]
        return nums
            
            