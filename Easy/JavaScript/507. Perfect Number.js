var checkPerfectNumber = function(num) {
    if(Math.floor(num % 2) != 0)
        return false;
    
    let n = 0;
    for(let i = 1; i <= Math.floor(num / 2); i++){
        if(Math.floor(num % i) == 0)
            n += i;
    }

    return n == num;
};
