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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();

        if(root == null)
            return new ArrayList<>();

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while(q.size() != 0)
        {
            Queue<TreeNode> temp = new LinkedList<>();
            while(q.size() != 0)
            {
                TreeNode t = q.poll();
                temp.offer(t);
            }
            List<Integer> curlvl = new ArrayList<>();
            while(temp.size() != 0)
            {
                TreeNode cur = temp.poll();
                if(cur != null)
                    curlvl.add(cur.val);
                if(cur.left == null && cur.right == null)
                    continue;
                if(cur.left != null)
                    q.offer(cur.left);
                if(cur.right != null)
                    q.offer(cur.right);
            }
            ans.add(curlvl);
        }
        return ans;
    }
}
