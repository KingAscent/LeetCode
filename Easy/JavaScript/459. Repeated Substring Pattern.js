var repeatedSubstringPattern = function(s) {
    // Append the string twice, then drop the first and last letter.
    // See if the result still includes the original string s.
    let dropped = (s + s).substring(1, (s.length * 2) - 1);
    return dropped.includes(s);
};
