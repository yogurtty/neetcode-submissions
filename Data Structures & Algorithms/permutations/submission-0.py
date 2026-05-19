class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        result = []
        for i, num in enumerate(nums):
            sub = self.permute(nums[:i]+nums[i+1:])
            for n in sub:
                n = n.insert(0, num)
            result.extend(sub)
        return result

        