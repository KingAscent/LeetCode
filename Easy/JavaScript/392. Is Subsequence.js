var isSubsequence = function(s, t) {
    if(s.length == 0)
        return true;
    if(t.length < s.length)
        return false;
    
    let sub = 0;

    for(let i = 0; i < t.length; i++){
        if(s[sub] === t[i])
            sub++;
        if(sub === s.length)
            return true;
    }

    return false;
};
