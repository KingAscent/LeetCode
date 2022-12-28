var repeatedCharacter = function(s) {
    const count = new Map();
    let twice = 'a';

    for(let i = 0; i < s.length; i++){
        if(!count.has(s.charAt(i)))
            count.set(s.charAt(i), 1);
        else{
            twice = s.charAt(i);
            break;
        }
    }

    return twice;
};
