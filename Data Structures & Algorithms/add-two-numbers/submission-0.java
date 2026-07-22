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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0);
        ListNode ans = res;
        int carry = 0;
        while(l1 != null && l2 != null)
        {
            int sum = carry;
            sum = sum + l1.val + l2.val;
            carry = sum/10;
            sum = sum%10;
            ListNode temp = new ListNode(sum);
            res.next = temp;
            res = res.next;
            l1 = l1.next;
            l2 = l2.next;
        }   
        if(l1 == null && l2 == null)
        {
            if(carry != 0)
            {
                ListNode temp = new ListNode(carry);
                res.next = temp;
                res = res.next;
            }
            return ans.next;
        }
        else
        {
            while( l1 != null)
            {
                int sum = carry;
                sum = sum + l1.val;
                carry = sum/10;
                sum = sum%10;
                ListNode temp = new ListNode(sum);
                res.next = temp;
                res = res.next;
                l1 = l1.next;
            }
            while( l2 != null)
            {
                int sum = carry;
                sum = sum + l2.val;
                carry = sum/10;
                sum = sum%10;
                ListNode temp = new ListNode(sum);
                res.next = temp;
                res = res.next;
                l2 = l2.next;
            }
        }
        if (carry == 1)
        {
            ListNode temp = new ListNode(carry);
            res.next = temp;
            res = res.next;
        }
        return ans.next;
    }
}
