class Solution {
    public int[] dailyTemperatures(int[] t) {
        int[] res = new int[t.length];
        for(int i=0; i<t.length; i++)
        {
            int cur = 1;
            for(int j=i+1; j<t.length; j++)
            {
                if(t[j]>t[i])
                {
                    res[i] = cur;
                    break;
                }
                else
                {
                    cur += 1;
                }
            }
        }
        return res;
    }
}
