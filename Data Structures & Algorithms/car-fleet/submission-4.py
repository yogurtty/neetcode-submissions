class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        res = sorted(zip(position, speed))
        for i in range(len(res)-1, -1, -1):
            time = (target-res[i][0])/(res[i][1])
            if not stack:
                stack.append(time)
                continue
            if stack[-1] < time:
                stack.append(time)
        return len(stack)
