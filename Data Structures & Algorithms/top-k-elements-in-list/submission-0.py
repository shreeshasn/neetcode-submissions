class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        print(d)
        res=[]

        for _ in range(k):
            maxx = -1
            max_i = 0
            for i in d.keys():
                if d[i] > maxx:
                    maxx = d[i]
                    max_i = i 
            res.append(max_i)
            d[max_i] = -1
        return res
            
        