class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums: List[int], target: int) -> int:
            high = len(nums) - 1
            low = 0;
            mid = (high + low) // 2
            if target > nums[high]:
                return -2 # too low
            elif target < nums[low]:
                return -3 # too high
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
            res = search(matrix[mid], target)
            if res >= 0:
                return True
            elif res == -3:
                high = mid - 1
            else:
                low = mid + 1
            mid = (high + low) // 2
        return False