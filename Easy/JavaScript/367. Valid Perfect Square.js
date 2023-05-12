var isPerfectSquare = function(num) {
    let i = 1;
    while(0 < num){
        num -= i;
        i += 2;
    }
    return num == 0;
};
