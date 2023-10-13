var differenceOfSums = function(n, m) {
    let num = 0;
    
    for(let i = 1; i <= n; i++){
        if(i % m != 0)
            num += i;
        else
            num -= i;
    }

    return num;
};
