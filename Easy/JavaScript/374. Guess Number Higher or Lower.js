var guessNumber = function(n) {
    if(n == 1)
        return 1;
    if(guess(n) == 0)
        return n;
    
    let first = 1;
    let last = n;
    let pick = 0;

    while(first < last){
        pick = first + (last - first) / 2;
        let temp = guess(pick);
        if(temp == 0){
            break;
        }else if(temp == -1){
            last = pick;
        }else{
            first = pick;
        }
    }

    return pick;
};
