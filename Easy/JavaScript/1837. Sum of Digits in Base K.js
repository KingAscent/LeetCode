var sumBase = function(n, k) {
    let count = 0;

    while(n != 0){
        count += n % k;
        n = Math.floor(n / k);
    }

    return count;
};
