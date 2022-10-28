class Solution {
    public boolean isPalindrome(int x) {
        // Convert x into a string
        String number = Integer.toString(x);
        
        // Go over the string seeing if it is a palindrome
        for(int i = 0; i < number.length() / 2; i++){
            if(number.charAt(i) != number.charAt(number.length() - i - 1))
                return false;
        }
        
        // The number is a palindrome, return true
        return true;
    }
}
