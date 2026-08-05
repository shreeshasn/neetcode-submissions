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
    private int height(TreeNode root)
    {
        if(root == null)
            return 0;
        return 1 + Math.max(height(root.left), height(root.right));
    }
    private int check(TreeNode root, int res)
    {
        if(root == null)
            return 0;
        int cur = height(root.left)+height(root.right);
        res = Math.max(cur, res);
        res = Math.max(  Math.max(check(root.left, res) , check(root.right,res)) , res );
        return res;
    }
    public int diameterOfBinaryTree(TreeNode root) {
        if(root == null)
            return 0;
        return check(root,0);
    }
}
