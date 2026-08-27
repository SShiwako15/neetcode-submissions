class TimeMap:

    def __init__(self):
        self.arr = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.arr:
            self.arr[key] = []
        self.arr[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        out = ""
        val = self.arr.get(key, [])
        l = 0
        r = len(val) - 1
        m = 0
        while l <= r:
            m = l + (r-l)//2
            if val[m][1] <= timestamp:
                l = m + 1
                out = val[m][0]
            else:
                r = m - 1
        return out