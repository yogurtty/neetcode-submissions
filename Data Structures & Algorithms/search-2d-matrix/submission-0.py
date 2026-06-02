class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(self, nums: List[int], target: int) -> int:
            high = len(nums) - 1
            low = 0;
            mid = (high + low) // 2
            while (high >= low):
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                mid = (high + low) // 2
            return -1
        high = len(matrix) - 1
        low = 0;
        mid = (high + low) // 2
        while (high >= low):
            res = search(self, matrix[mid], target)
            if res != -1:
                return True
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
            mid = (high + low) // 2
        return False