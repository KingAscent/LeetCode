var countGoodSubstrings = function(s) {
    if(s.length <= 2)
        return 0;
    let count = 0;

    for(let i = 0; i < s.length - 2; i++){
        if(s.charAt(i) != s.charAt(i + 1)
        && s.charAt(i + 1) != s.charAt(i + 2)
        && s.charAt(i + 2) != s.charAt(i))
            count++;
    }

    return count;
};
