class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 0
        map = {}
        for num in nums:
            if num in map:
                continue
            length = map.get(num+1,0) + map.get(num-1,0) + 1
            map[num] = length 
            map[num - map.get(num-1,0)] = length
            map[num + map.get(num+1,0)] = length
            
            if maxi < map[num]:
                    maxi = map[num]
        return maxi
            
            
        