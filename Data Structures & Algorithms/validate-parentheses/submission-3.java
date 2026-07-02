class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) { // meaning some strangler bracket is present
            return false;
        }

        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') 
            {
                stack.push(c);
            } 
            else 
            {
                if (stack.isEmpty()) // meaning there was no earlier opening bracket
                {
                    return false;
                }
                
                char top = stack.pop();
                if ((c == ')' && top != '(') || 
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) //meaning there is no valid opening bracket
                {
                    return false;
                }
            }
        }

        return stack.isEmpty(); // iff the exp is valid, stack will be empty, 
                                // or else the bracket pairs would be odd, somehow.
    }
}
