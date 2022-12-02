var lengthOfLongestSubstring = function(s) {
    let longest = 0;
    let word = new Set();

    // Go over the string, comparing each character
    // to the next. If a character is new, place it
    // into the Set. Once a repeat is found,
    // the size of the Set is the length of the substring
    for(let i = 0; i < s.length; i++){
        for(let j = i; j < s.length; j++){
            if(word.has(s.charAt(j))){
                j = s.length;
            }else{
                word.add(s.charAt(j));
            }
        }
        longest = Math.max(word.size, longest);
        word.clear();
    }

    return longest;
};
