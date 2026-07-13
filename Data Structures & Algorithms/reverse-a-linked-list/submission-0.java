/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addFirst(ListNode head, int val)
    {
        ListNode temp = new ListNode(val);
        temp.next = head;
        return temp;
    }
    public ListNode reverseList(ListNode head) {
        if(head == null)
            return head;
        if(head.next == null)
            return head;
        ListNode cur = head;
        ListNode ans = new ListNode(head.val);
        cur = cur.next;
        while(cur!=null)
        {
            ans = addFirst(ans, cur.val);
            cur = cur.next;
        }
        return ans;
    }
}
