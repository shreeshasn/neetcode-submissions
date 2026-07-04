class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        for(String i : tokens)
        {
            if(i.equals("+"))
            {
                stack.push(stack.pop()+stack.pop());
            }
            else if(i.equals("-"))
            {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b-a);
            }
            else if(i.equals("/"))
            {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b/a);
            }
            else if(i.equals("*"))
            {
                stack.push(stack.pop()*stack.pop());
            }
            else
            {
                stack.push(Integer.parseInt(i));
            }
        }
        return stack.pop();
    }
}
