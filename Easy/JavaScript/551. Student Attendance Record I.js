var checkRecord = function(s) {
    let countAbsent = 0;
    
    if(s.includes("LLL"))
        return false;

    for(let i = 0; i < s.length; i++){
        if(s[i] == 'A')
            countAbsent++;
    }

    return countAbsent < 2;
};
