class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        stack = set()
        min = 1001
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if len(stack) < k:
                stack.add(num)
                if min == 1001:
                    min = num
                else:
                    if counts.get(min) > counts.get(num):
                        min = num
            else:
                for item in stack:
                    if counts.get(min) > counts.get(item):
                        min = item
                if counts.get(min) < counts.get(num) and num not in stack:
                    stack.add(num)
                    stack.remove(min)
                    min = num

        return list(stack)
                
