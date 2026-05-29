class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        max_time = 0
        fleets = 0
        res = sorted(zip(position, speed))
        for i in range(len(res)-1, -1, -1):
            time = (target-res[i][0])/(res[i][1])
            
            if max_time < time:
                max_time = time
                fleets += 1
        return fleets
