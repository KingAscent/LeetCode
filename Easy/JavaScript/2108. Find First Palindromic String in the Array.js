var firstPalindrome = function(words) {
    let palindrome = "";
    let palindromeFound = false;

    words.forEach(s => {
        let left = 0;
        let right = s.length - 1;
        let isPalindrome = true;

        // Use 2 pointers to compare each character in each word
        while(left <= right){
            if(s[left] !== s[right])
                isPalindrome = false;
            left++;
            right--;
        }

        // If the word is a palindrome, store it in the palidrome variable
        if(isPalindrome && !palindromeFound){
            palindrome = s;
            palindromeFound = true;
        }
    })

    return palindrome;
};
