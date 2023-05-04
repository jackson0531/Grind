# stores key, value is value and timestamp
class TimeMap:

    def __init__(self):
        self.map1 = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map1[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        row = self.map1[key]
        if (len(row)==0): 
            return ""
        l, r = 0, len(row)-1
        while l<r: 
            mid = (l+r)//2
            if timestamp <= row[mid][1]: 
                r = mid
            else: 
                l = mid+1
        if row[l][1]<=timestamp: 
            return row[l][0]
        elif timestamp<row[l][1] and l-1>=0: 
            return row[l-1][0]
        else: 
            return ""
