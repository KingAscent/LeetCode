var isAnagram = function(s, t) {
    if(s.length != t.length)
        return false;
    
    let sChars = [];
    let tChars = [];

    for(let i = 0; i < s.length; i++){
        sChars[i] = s.charAt(i);
        tChars[i] = t.charAt(i);
    }
    sChars.sort();
    tChars.sort();

    return sChars.toString() == tChars.toString();
};
