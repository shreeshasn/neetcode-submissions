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

    // Main merge sort function
    private ListNode mergeSort(ListNode head) {
        // Base case: if list is empty or has only one node
        if (head == null || head.next == null) {
            return head;
        }

        // 1. Split the list into two halves
        ListNode middle = getMiddle(head);
        ListNode nextToMiddle = middle.next;
        middle.next = null; // Break the link to split the list

        // 2. Recursively sort both halves
        ListNode left = mergeSort(head);
        ListNode right = mergeSort(nextToMiddle);

        // 3. Merge the sorted halves together
        return sortedMerge(left, right);
    }

    // Helper function to merge two sorted linked lists
    private ListNode sortedMerge(ListNode a, ListNode b) {
        // Base cases
        if (a == null) return b;
        if (b == null) return a;

        ListNode result;
        
        // Pick either a or b, and recur
        if (a.val <= b.val) {
            result = a;
            result.next = sortedMerge(a.next, b);
        } else {
            result = b;
            result.next = sortedMerge(a, b.next);
        }
        return result;
    }

    // Helper function to find the middle node using tortoise and hare approach
    private ListNode getMiddle(ListNode head) {
        if (head == null) return null;

        ListNode slow = head;
        ListNode fast = head;

        // Move fast by two steps and slow by one step
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public ListNode mergeKLists(ListNode[] lists) {
        System.out.println(lists);
        if( lists.length == 0 )
            return (ListNode) null;
        int k = lists.length;
        int i = 1;
        ListNode head = lists[0];
        ListNode cur = head;
        while(cur.next != null)
            cur = cur.next;
        while(k >= 0 && i < lists.length)
        {
            cur.next = lists[i];
            cur = cur.next;
            while (cur.next != null)
                cur = cur.next;
            k--;
            i++;
        }
        head = mergeSort(head); 
        return head;
    }
}
