var furthestDistanceFromOrigin = function(moves) {
    let countL = 0;
    let countR = 0;
    let countBlanks = 0;

    for(let i = 0; i < moves.length; i++){
        if(moves.charAt(i) == 'L')
            countL++;
        else if(moves.charAt(i) == 'R')
            countR++;
        else
            countBlanks++;
    }

    return Math.abs(countL - countR) + countBlanks;
};
