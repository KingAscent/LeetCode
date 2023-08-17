var countSegments = function(s) {
    let count = 0;

    for(let i = 0; i < s.length; i++){
        if((i == 0 || s.charAt(i - 1) == ' ') && s.charAt(i) != ' ')
            count++;
    }

    return count;
};
