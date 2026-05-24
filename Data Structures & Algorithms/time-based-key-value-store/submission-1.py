class TimeMap:

    def __init__(self):
        self.tm = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        l= [value,timestamp]
        if key not in self.tm:
            self.tm[key] = []
        self.tm[key].append(l)
        print(self.tm)

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm :
             return ""
        l= 0  
        r = len(self.tm[key])-1
        result = -1
        while(l<=r):
            mid = (l+r)//2
            print(mid)
            print(self.tm[key][mid])
            
            if(timestamp >= self.tm[key][mid][1]):
                result = mid
                l = mid+1
            else:
                r= mid-1
        if result == -1:
            return ""
        return self.tm[key][result][0]
                    
