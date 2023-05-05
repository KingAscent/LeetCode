var isVowel = function(c){
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
};

var maxVowels = function(s, k) {
    let maxSub = 0;
    let window = 0;

    for(let i = 0; i < s.length; i++){
        if(isVowel(s.charAt(i)))
            window++;
        maxSub = Math.max(maxSub, window);

        // Move the window to the right one character
        if(k - 1 <= i && isVowel(s.charAt(i - k + 1)))
            window--;
    }

    return maxSub;
};
