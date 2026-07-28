class Solution:
    def checkInclusion(self, s1, s2) -> bool:
        ds1 = Counter(s1)
        w = len(s1)
        for i in range(0,len(s2)-w+1):
            cur = s2[i:i+w]
            print(cur)
            ds2 = Counter(cur)
            if ds2 == ds1:
                return True
        return False