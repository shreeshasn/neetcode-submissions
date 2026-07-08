class Solution:
    def largestRectangleArea(self, nums):
        left = []
        st = []
        for i in range(len(nums)):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if not st:
                left.append(-1)
            else:
                left.append(st[-1])
            st.append(i)
        print(left)

        n =len(nums)
        right = [n]*n
        st = []
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st and nums[st[-1]] < nums[i]:
                right[i]=st[-1]
            st.append(i)
        print(right)
    
        res = 0
        for i in range(len(nums)):
            res = max(res  , nums[i]*(right[i]-left[i]-1))

        return res
            