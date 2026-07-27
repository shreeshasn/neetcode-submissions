/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        HashMap<Node, Node> old = new HashMap<>();
        Node cur = head;
        while(cur != null )
        {
            Node temp = new Node(cur.val);
            old.put(cur, temp);
            cur = cur.next;
        }
        for(Node org : old.keySet())
        {
            Node c = old.get(org);
            if(org.next != null)
                c.next = old.get(org.next);
            if(org.random != null)
                c.random = old.get(org.random);
            old.put(org , c);
        }
        return old.get(head);
    }
}
