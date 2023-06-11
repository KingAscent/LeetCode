var minTimeToType = function(word) {
    let count = word.length;
    let prev = 'a';

    for(let i = 0; i < word.length; i++){
        let curr = word.charAt(i);
        let diff = Math.abs(curr.charCodeAt(0) - prev.charCodeAt(0));
        count += Math.min(diff, 26 - diff);
        prev = curr;
    }

    return count;
};
