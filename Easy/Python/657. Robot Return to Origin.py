var judgeCircle = function(moves) {
    let x = 0;
    let y = 0;

    for(let i = 0; i < moves.length; i++){
        if(moves.charAt(i) == 'U')
            y++;
        if(moves.charAt(i) == 'D')
            y--;
        if(moves.charAt(i) == 'L')
            x--;
        if(moves.charAt(i) == 'R')
            x++;
    }

    return(x == 0 && y == 0);
};
