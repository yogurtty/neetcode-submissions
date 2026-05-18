class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 0
        map = {}
        for num in nums:
            if num+1 in map and num-1 in map:
                map[num+1] |= map[num-1]
                map[num-1] = map[num+1]
                map[min(map[num+1])] = map[num+1]
                map[max(map[num+1])] = map[num+1]
            if num+1 in map:
                map[num] = map[num+1]
            elif num-1 in map:
                map[num] = map[num-1] 
            map.setdefault(num, set()).add(num) 
            if maxi < len(map[num]):
                    maxi = len(map[num])
        return maxi
            
            
        