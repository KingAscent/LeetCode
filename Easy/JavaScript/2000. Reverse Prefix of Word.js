var reversePrefix = function(word, ch) {
    var s = word.split("");

    for(let i = 0 ; i <= word.indexOf(ch); i++){
        s[i] = word.charAt(word.indexOf(ch) - i);
    }

    return s.join("");
};
