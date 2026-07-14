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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1==null)
            return list2;
        if(list2==null)
            return list1;
        ListNode newhead;
        ListNode head;
        ListNode l1 = list1;
        ListNode l2 = list2;
        if(l1.val < l2.val)
        {
            newhead = new ListNode(l1.val);
            l1 = l1.next;
        }
        else
        {
            newhead = new ListNode(l2.val);
            l2 = l2.next;
        }
        head = newhead;
        while(l1!=null && l2!=null)
        {
            if(l1.val < l2.val)
            {
                newhead.next =  new ListNode(l1.val);
                newhead = newhead.next;
                l1 = l1.next;
            }
            else
            {
                newhead.next = new ListNode(l2.val);
                newhead = newhead.next;
                l2 = l2.next;
            }
        }
        if(l1==null)
        {
            while(l2!=null)
            {
                newhead.next = new ListNode(l2.val);
                newhead = newhead.next;
                l2 = l2.next;
            }
        }
        if(l2==null)
        {
            while(l1!=null)
            {
                newhead.next = new ListNode(l1.val);
                newhead = newhead.next;
                l1 = l1.next;
            }
        }
        return head;
    }
}