/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private int check(TreeNode root)
    {
        if(root == null)
            return -1;
        int l = check(root.left);
        int r = check(root.right);
        return 1 + Math.max(l,r);
    }
    public boolean isBalanced(TreeNode root) {
        if(root == null || (root.left == null && root.right == null))
            return true;
        int l = check(root.left);
        int r = check(root.right);
        return (Math.abs(l-r) <= 1) && isBalanced(root.left) && isBalanced(root.right);
    }
}
