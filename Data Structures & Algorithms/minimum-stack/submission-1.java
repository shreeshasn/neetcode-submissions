class MinStack {

    List<Integer> stack = new ArrayList<>();
    int top = -1;

    public MinStack() {
        
    }
    
    public void push(int val) {
        stack.add(val);
        top = top + 1;
    }
    
    public void pop() {
        stack.remove(top);
        top = top - 1;
    }
    
    public int top() {
        return stack.get(top);
    }
    
    public int getMin() {
        int getmin = stack.get(top);
        for(int i : stack)
        {
            getmin = Math.min(getmin , i);
        }
        return getmin;
    }
}
