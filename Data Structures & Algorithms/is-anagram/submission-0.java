class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sarr = s.toCharArray();
        Arrays.sort(sarr);
        String new_s = new String(sarr);
        char[] tarr = t.toCharArray();
        Arrays.sort(tarr);
        String new_t = new String(tarr);
        return new_s.equals(new_t);
                
    }
}
