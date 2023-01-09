var fib = function(n) {
    if(n <= 1)
        return n;
    
    let a = 0;
    let b = 1;
    for(let i = 1; i < n; i++){
        let temp = a;
        a = b;
        b += temp;
    }

    return b;
};
