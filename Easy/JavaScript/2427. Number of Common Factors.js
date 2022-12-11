var commonFactors = function(a, b) {
    let factors = 0;
    let max = Math.min(a, b);

    for(let i = 1; i <= max; i++){
        if(a % i == 0 && b % i == 0)
            factors++;
    }

    return factors;
};
