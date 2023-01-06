var truncateSentence = function(s, k) {
    var words = s.split(" ");
    let truncated = "";

    for(let i = 0; i < k; i++){
        truncated += words[i];
        if(i + 1 < k)
            truncated += " ";
    }

    return truncated;
};
