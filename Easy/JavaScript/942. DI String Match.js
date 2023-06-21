var diStringMatch = function(s) {
    let n = s.length;
    let perm = Array(n + 1).fill(0);
    let start = 0;
    let end = n;

    for(let i = 0; i < s.length; i++){
        if(s.charAt(i) == 'I')
            perm[i] = start++;
        else
            perm[i] = end--;
    }
    perm[n] = start;

    return perm;
};
