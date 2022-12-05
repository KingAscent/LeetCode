var reverseWords = function(s) {
    // Get all of the words separated by their whitespaces
    let split = s.split(" ");

    // For each word, split each character, reverse their order, and then join them together
    for(let i = 0; i < split.length; i++){
        split[i] = split[i].split("").reverse().join("");
    }
    // Return every word in the split array, joined together by whitespaces
    return split.join(" ");
};
