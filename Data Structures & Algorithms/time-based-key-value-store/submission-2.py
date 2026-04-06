class TimeMap:

    def __init__(self):
        self.vals = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.vals.keys():
            self.vals[key].append([timestamp, value])
        else:
            self.vals[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        #get list
        
        if key not in self.vals.keys():
            return ""

        ref = self.vals[key]

        l = 0
        r = len(ref) - 1

        while l <= r:
            mid = (l + r) // 2
            if self.vals[key][mid][0] == timestamp:
                return self.vals[key][mid][1]
            elif self.vals[key][mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if r < 0:
           return ""
        return self.vals[key][r][1]
