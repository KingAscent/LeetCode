var halvesAreAlike = function(s) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let front = 0;
    let back = 0;

    for(let i = 0; i < s.length / 2; i++){
        if(vowels.has(s.charAt(i).toLowerCase()))
            front++;
        if(vowels.has(s.charAt(i + s.length / 2).toLowerCase()))
            back++;
    }

    return front == back;
};
