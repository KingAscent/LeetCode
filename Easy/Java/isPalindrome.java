class Solution {
    public boolean isPalindrome(int x) {
        // Convert x to a string, then find its length
        String str = String.valueOf(x);
        int length = str.length();
        
        // Use a for loop to go over half of the string,
        // making sure that it is the same on both the
        // front and end of the string
        for(int i = 0; i < length / 2; i++){
            if(str.charAt(i) != str.charAt(length - i - 1))
                return false;
        }
        return true;
    }
}
