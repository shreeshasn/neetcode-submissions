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
    private TreeNode lca(TreeNode root, TreeNode p, TreeNode q)
    {
        if(root == null || root.val == p.val || root.val == q.val ||  (p.val<root.val && root.val<q.val) )
            return root;
        if( root.val > p.val && root.val > q.val)
            root = lca(root.left, p, q);
        if( root.val < p.val && root.val < q.val)
            root = lca(root.right, p, q);
        return root;
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return lca(root,p,q);
    }
}
