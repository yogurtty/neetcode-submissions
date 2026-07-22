class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max = 0
        for num in piles:
            if num > max:
                max = num
        
        low = 1
        high = max
        
        k = int((low+high)/2);
        total = 0;
        while (low <= high):
            for num in piles:
                total += int(num/k)
                if (num % k != 0):
                    total = total + 1
            if k < max and total <= h:
                max = k
                high = k - 1
            else:
                low = k + 1
            k = int((low+high)/2);
            total = 0
        return max
            




        
        


        