class Solution {
    public String firstPalindrome(String[] words) {
        for(String s : words){
            int left = 0;
            int right = s.length() - 1;
            boolean isPalindrome = true;
            
            // Use 2 pointers to compare each character in each word
            while(left <= right){
                if(s.charAt(left) != s.charAt(right))
                    isPalindrome = false;
                left++;
                right--;
            }

            // If the word is a palindrome, return it
            if(isPalindrome)
                return s;
        }

        return "";
    }
}
