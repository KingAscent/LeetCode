var lastRemaining = function(n) {
    let last = 1;
    if(n == 1){
        return last;
    }else{
        let temp = lastRemaining(Math.floor(n / 2));
        last = 2 * (Math.floor(n / 2) - temp + 1);
    }
    return last;
};
