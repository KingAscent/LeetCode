class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        HashSet<Character> set = new HashSet();
        
        // Go over the string, comparing each character
        // to the next. If a character is new, place it
        // into the HashSet. Once a repeat is found,
        // the size of the HashSet is the length of substring
        for(int i = 0; i < s.length(); i++){
            for(int j = i; j < s.length(); j++){
                if(set.contains(s.charAt(j))){
                    j = s.length();
                }else{
                    set.add(s.charAt(j));
                }
            }
            longest = Math.max(set.size(), longest);
            set.clear();
        }
        
        return longest;
    }
}
