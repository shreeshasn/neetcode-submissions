class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:
        #     return 0
        # resmax = 1
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         cur = s[i:j+1]
        #         if len(set(cur)) == len(cur):
        #             resmax = max(resmax , len(cur))
        # return resmax

        if not s:
            return 0

        if len(set(s))==len(s):
            return len(s)

        w = len(s)-1
        while w>0:
            i = 0
            j = i+w
            while i<(len(s)-w) and j<len(s):
                cur = s[i:j+1]
                if len(set(cur)) == len(cur):
                    return len(cur)
                i+=1
                j+=1
            w-=1
        return 1


