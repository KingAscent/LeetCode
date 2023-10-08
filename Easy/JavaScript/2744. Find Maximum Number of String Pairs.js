var maximumNumberOfStringPairs = function(words) {
    let count = 0;

    for(let i = 0; i < words.length; i++){
        for(let j = i + 1; j < words.length; j++){
            if(words[i].charAt(0) == words[j].charAt(1) && words[i].charAt(1) == words[j].charAt(0)){
                count++;
                break;
            }
        }
    }

    return count;
};
