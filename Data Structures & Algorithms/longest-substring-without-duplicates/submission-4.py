class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        resmax = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                cur = s[i:j+1]
                if len(set(cur)) == len(cur):
                    resmax = max(resmax , len(cur))
        return resmax