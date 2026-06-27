class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        if(nums.length==1 || nums.length==0)
            return nums.length;
        if(nums.length==2)
        {
            if(nums[0]==nums[1])
                return 1;
            return (nums[0]+1==nums[1]) ? 2 : 1;
        }
        int max=1; int maxx=1;
        for(int i=1; i<nums.length; i++)
        {
            if(nums[i]==nums[i-1]+1)
            {
                maxx=maxx+1;
                if(maxx > max)
                    max=maxx;
            }
            else if(nums[i]==nums[i-1])
            {
                continue;
            }
            else
            {
                maxx=1;
            }
        }
        return max;
    }   
}