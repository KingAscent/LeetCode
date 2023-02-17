var prefixCount = function(words, pref) {
    let count = 0;

    words.forEach(s => {
        if(s.indexOf(pref) == 0)
            count++;
    })

    return count;
};
