var isPalindrome = function(s) {
    s = s.toLowerCase().replaceAll(/[^0-9a-zA-Z]+/gmi,"");
    let start = 0;
    let end = s.length - 1;
    while(start <= end){
        if(s.charAt(start) != s.charAt(end))
            return false;
        start++;
        end--;
    }
    return true;
};
