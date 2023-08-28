class Solution {
    public boolean repeatedSubstringPattern(String s) {
        // Append the string twice, then drop the first and last letter.
        // See if the result still contains the original string s.
        String dropped = (s + s).substring(1, (s.length() * 2) - 1);
        return dropped.contains(s);
    }
}
