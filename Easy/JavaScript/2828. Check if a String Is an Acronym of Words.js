var isAcronym = function(words, s) {
    let sb = [];

    for(let word of words){
        sb.push(word.charAt(0));
    }

    return sb.join("") === (s);
};
