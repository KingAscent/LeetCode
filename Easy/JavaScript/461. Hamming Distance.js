var hammingDistance = function(x, y) {
    let num = 0;

    while(0 < x || 0 < y){
        if(Math.floor(x % 2 ) != Math.floor(y % 2))
            num++;
        x /= 2;
        y /= 2;
    }

    return num;
};
