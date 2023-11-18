var maxRepeating = function(sequence, word) {
    let count = 0;
    let rep = word;

    while(sequence.includes(rep)){
        count++;
        rep += word;
    }

    return count;
};
