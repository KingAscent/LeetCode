var areOccurrencesEqual = function(s) {
    let freq = {};
    
    for(let c of s){
        freq[c] = (freq[c] || 0) + 1;
    }

    let max = freq[s[0]];
    for(let c in freq){
        if(freq[c] != max)
            return false;
    }

    return true;
};
