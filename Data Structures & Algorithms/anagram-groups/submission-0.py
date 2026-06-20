class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for i in strs:
            j="".join(sorted(i))
            if j in d:
                l=d[j]
                l.append(i)
                d[j]=l
            else:
                l=[]
                l.append(i)
                d[j]=l
        for x in d.keys():
            res.append(d[x])
        return res