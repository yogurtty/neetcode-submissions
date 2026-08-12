class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1 
        low = 0
        total = (len(nums1) + len(nums2)) // 2
        high = len(nums2)
        while high >= low:
            mid2 = (high + low) // 2
            mid1 = total - mid2

            left1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            right1 = nums1[mid1] if mid1 < len(nums1) else float("inf")

            left2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            right2 = nums2[mid2] if mid2 < len(nums2) else float("inf")

            
            if left2 > right1:
                high = mid2 - 1

    
            elif left1 > right2:
                low = mid2 + 1

            else:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(right1, right2)

                return (max(left1, left2) + min(right1, right2)) / 2



                
            
        return 0.0
            