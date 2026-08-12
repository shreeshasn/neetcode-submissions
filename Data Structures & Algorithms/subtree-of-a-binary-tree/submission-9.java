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
    List<TreeNode> c = new ArrayList<>();
    private void check(TreeNode root, int x)
    {
        if(root == null)
            return;
        if(root.val == x)
            c.add(root);
        check(root.left,x);
        check(root.right,x);
    }
    private boolean checkS(TreeNode root, TreeNode sub)
    {
        if(root == null && sub == null)
            return true;
        if( (root == null && sub != null) || (root != null && sub == null) )
            return false;
        if(root.val != sub.val)
            return false;
        return (true) && checkS(root.left,sub.left) && checkS(root.right, sub.right);
    }
    public boolean isSubtree(TreeNode root, TreeNode sub) {
        check(root, sub.val);
        for(TreeNode n : c)
            if(checkS(n, sub))
                return true;
        return false;
    }
}
