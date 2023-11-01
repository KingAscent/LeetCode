var isHappy = function(n) {
    while(n != 1 && n != 4){
        let sum = n;
        n = 0;
        while(sum != 0){
            let temp = Math.floor(sum % 10);
            n += temp * temp;
            sum = Math.floor(sum / 10);
        }
    }

    return n == 1;
};
