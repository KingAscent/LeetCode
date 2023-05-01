var mergeAlternately = function(word1, word2) {
    let word3 = "";
    let i = 0;

    while(i != word1.length && i != word2.length){
        word3 += word1.charAt(i);
        word3 += word2.charAt(i);
        i++;
    }
    if(i < word1.length)
        word3 += word1.substring(i);
    if(i < word2.length)
        word3 += word2.substring(i);

    return word3;
};
