class Solution {
    public char findTheDifference(String s, String t) {
        char added = 0;

        for(char c : s.toCharArray())
            added ^= c;
        for(char c : t.toCharArray())
            added ^= c;

        return added;
    }
}
