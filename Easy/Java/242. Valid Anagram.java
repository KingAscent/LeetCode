class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;
        
        char[] sChars = new char[s.length()];
        char[] tChars = new char[t.length()];

        for(int i = 0; i < s.length(); i++){
            sChars[i] = s.charAt(i);
            tChars[i] = t.charAt(i);
        }
        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }
}
