class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        d= {}
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                cur = s[i:j+1]
                # print(cur)
                if cur == cur[::-1]:       
                    count += 1
        return count