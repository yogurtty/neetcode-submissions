class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        for i in range (0, len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -1 * nums[i]:
                    result.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                    continue
                if nums[j] + nums[k] < -1 * nums[i]:
                    j += 1
                else:
                    k -= 1
                

                    
        return list(result)

        