class Solution {
    public int countAsterisks(String s) {
        int count = 0;
        boolean isBarred = false;

        // Look through the string, when a bar is found
        // ignore any asterisks found
        for(int i = 0; i < s.length(); i++){
            if(!isBarred && s.charAt(i) == '|')
                isBarred = true;
            else if(isBarred && s.charAt(i) == '|')
                isBarred = false;
            if(!isBarred && s.charAt(i) == '*')
                count++;
        }

        return count;
    }
}
