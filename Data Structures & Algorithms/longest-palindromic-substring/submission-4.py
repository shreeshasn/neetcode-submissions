class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or s == s[::-1]:
            return s
        res = 1
        ans = s[0]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                cur = s[i:j+1]
                if cur == cur[::-1] and len(cur) >= res:
                    res = len(cur)
                    ans = cur
        return ans