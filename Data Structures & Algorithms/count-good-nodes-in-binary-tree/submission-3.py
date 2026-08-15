# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global count
        count = 0
        def check(self, root, maxSoFar):
            if root is None:
                return
            if root.left == None and root.right == None:
                if maxSoFar <= root.val:
                    global count 
                    count += 1
                return
            
            if maxSoFar <= root.val:
                count += 1

            maxSoFar = max(maxSoFar , root.val)
            check(self, root.left , maxSoFar)
            check(self, root.right , maxSoFar)

        check(self, root, -101)
        return count
