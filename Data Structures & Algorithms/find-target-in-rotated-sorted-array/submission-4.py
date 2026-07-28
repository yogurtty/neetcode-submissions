class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = int((left+right)/2)
        if target <= nums[right]:
            rivot = True
        else:
            rivot = False
        if rivot:
            while left <= right:
                mid = int((left+right)/2)
                if nums[mid] == target:
                    return mid
                if nums[mid] <= nums[len(nums)-1]:
                    if nums[mid] < target:
                        left = mid+1
                    else:
                        right = mid-1
                else:
                    left = mid+1
        else:
            while left <= right:
                mid = int((left+right)/2)
                if nums[mid] == target:
                    return mid
                if nums[mid] >= nums[len(nums)-1]:
                    if nums[mid] < target:
                        left = mid+1
                    else:
                        right = mid-1
                else:
                    right = mid-1
                
        return -1

                    

            


            
        