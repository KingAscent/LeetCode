var balancedStringSplit = function(s) {
    let countR = 0;
    let countL = 0;
    let count = 0;

    for(let i = 0; i < s.length; i++){
        if(s.charAt(i) == 'L')
            countL++;
        else
            countR++;
        if(countR == countL && countR != 0){
            count++;
            countL = 0;
            countR = 0;
        }
    }

    return count;
};
