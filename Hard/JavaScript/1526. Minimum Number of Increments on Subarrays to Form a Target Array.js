var minNumberOperations = function(target) {
    let ops = 0;
    let prev = 0;

    for(let n of target){
        if(prev < n)
            ops += n - prev;
        prev = n;
    }

    return ops;
};
