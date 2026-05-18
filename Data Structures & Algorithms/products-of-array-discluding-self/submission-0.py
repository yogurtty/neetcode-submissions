class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        product = 1
        for i in range(0, len(nums)):
            for j, num in enumerate(nums):
                if i != j:
                    product *= num
            output[i] = product
            product = 1
        return output
            
            