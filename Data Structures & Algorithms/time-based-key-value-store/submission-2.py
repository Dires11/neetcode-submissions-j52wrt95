class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ''
        values = self.data[key]
        l = 0 
        r = len(values)-1
        out = ''
        while l <= r:
            mid = (l+r)//2
            if values[mid][0] <= timestamp:
                out = values[mid][1]
                l = mid+1
            else:
                r = mid-1  
        return out


