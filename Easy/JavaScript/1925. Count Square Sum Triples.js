var countTriples = function(n) {
    let count = 0;

    for(let i = 1; i < n - 1; i++){
        for(let j = i + 1; j < n; j++){
            for(let k = j + 1; k < n + 1; k++){
                if((i * i) + (j * j) == (k * k))
                    count += 2;
            }
        }
    }

    return count;
};
