class TimeMap:

    def __init__(self):
        self.t = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.t.get(key,"") == "":
            d = {}
            d[timestamp] = value
            self.t[key] = d
        else:
            temp = self.t[key]
            temp[timestamp] = value
            self.t[key] = temp 
        print(self.t)

    def get(self, key: str, timestamp: int) -> str:
        print(self.t)
        if key in self.t:
            cur = self.t[key]
            if cur.get(timestamp,"") == "":
                l = sorted(cur.keys())
                print(l)
                if timestamp < l[0]:
                    return ""
                else:
                    actual = l[0]
                    for i in l[1:]:
                        if i <= timestamp:
                            actual = i
                        else:
                            return cur[actual]
                    return cur[actual] 
            else:
                return cur[timestamp]
        else:
            return ""