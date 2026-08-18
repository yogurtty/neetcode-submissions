class TimeMap:

    def __init__(self):
        self.mao = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mao:
            self.mao[key].append([timestamp, value])
        else:
            self.mao[key] = [[0, ""]]
            self.mao[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.mao.get(key)
        if not lst or timestamp < lst[1][0]:  # If it's smaller than the first *real* element
            return ""
            
        l = 0
        r = len(lst) - 1
        res = ""
        
        while l <= r:
            m = (l + r) // 2
            if lst[m][0] <= timestamp:
                res = lst[m][1]
                l = m + 1
            else:
                r = m - 1
                
        return res
