class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int count = 0;

        for(String s : words){
            // Check if each character in String s is present in allowed
            for(int i = 0; i < s.length(); i++){
                // If it isn't, exit the loop
                // If each letter is present in allowed, increase count by 1
                if(allowed.indexOf(s.charAt(i)) == -1)
                    break;
                if(i == s.length() - 1)
                    count++;
            }
        }

        return count;
    }
}
