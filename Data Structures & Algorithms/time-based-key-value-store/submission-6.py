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
        if self.mao.get(key) is None or timestamp < self.mao.get(key)[1][0]:
            return ""
        l = 0
        r = len(self.mao.get(key)) - 1
        m = int((l + r) / 2)
        res = ""
        while l <= r:
            m = int((l + r) / 2)
            if self.mao.get(key)[m][0] <= timestamp:
                res = self.mao.get(key)[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        

        
