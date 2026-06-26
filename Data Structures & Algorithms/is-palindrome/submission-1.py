class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for i in s:
            if i.isalnum():
                res = res + i
        print(res)
        return res == res[::-1]