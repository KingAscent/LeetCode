var percentageLetter = function(s, letter) {
    let count = 0;

    for(let i = 0; i < s.length; i++){
        if(s.charAt(i) === letter)
            count++;
    }

    return Math.floor((count / s.length) * 100);
};
