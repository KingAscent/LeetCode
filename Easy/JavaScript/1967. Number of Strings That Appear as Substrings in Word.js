var numOfStrings = function(patterns, word) {
    let count = 0;

    patterns.forEach(s => {
        if(word.includes(s))
            count++;
    })

    return count;
};
