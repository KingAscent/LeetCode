var maxPower = function(s) {
    let max = 0;
    let n = 0;

    for(let i = 0; i < s.length - 1; i++){
        if(s.charAt(i) == s.charAt(i + 1))
            n++;
        else
            n = 0;
        max = Math.max(max, n);
    }

    return Math.max(max, n) + 1;
};
