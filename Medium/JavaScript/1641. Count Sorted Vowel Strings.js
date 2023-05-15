var countVowelStrings = function(n) {
    let a = e = i = o = u = 1;

    for(let j = 1; j < n; j++){
        a += e + i + o + u;
        e += i + o + u;
        i += o + u;
        o += u;
        // u doesn't change
    }

    return a + e + i + o + u;
};
