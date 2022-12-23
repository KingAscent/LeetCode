var replaceDigits = function(s) {
        var word = s.split("");

        for(let i = 1; i < word.length; i += 2){
            word[i] = shift(String(word[i - 1]), Number(word[i]));
        }

        return word.join("");
};

function shift(c, x) {
    return String.fromCharCode(c.charCodeAt(0) + x);
}
