class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if(head == null || head.next == null)
            return head;
        int l = 0;
        ArrayList<ListNode> temp = new ArrayList<>();
        ListNode cur = head;
        while(cur != null)
        {
            l += 1; 
            ListNode t = new ListNode(cur.val);
            temp.add(t);
            cur = cur.next;
        }
        int total = l;
        if(l%k != 0)
            total = total - total%k;
        System.out.print("TOTAL: "+total);
        for(int x=0; x<total;x+=k)
        {
            int i = x;
            int j = x+k-1;
            while(i<=j)
            {   
                ListNode tempi = temp.get(i);
                ListNode tempj = temp.get(j);
                tempj = temp.set(i, tempj);
                tempi = temp.set(j, tempi);
                i+=1;
                j-=1;
            }
        }
        ListNode res = temp.get(0);
        cur = res;
        for(int i=1; i<temp.size(); i++)
        {
            cur.next = temp.get(i);
            cur = cur.next; 
        }
        return res;
    }
}
