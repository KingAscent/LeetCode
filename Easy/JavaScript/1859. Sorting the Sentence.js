var sortSentence = function(s) {
    let words = s.split(" ");
    let sentence = [];

    words.forEach((word) => {
        let n = word.length - 1;
        sentence[word.charAt(n) - '1'] = word.substring(0, n);
    })

    return sentence.join(" ");
};
