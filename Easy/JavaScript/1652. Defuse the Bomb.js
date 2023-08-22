var decrypt = function(code, k) {
    let n = code.length;
    let df = Array(n).fill(0);

    if(0 < k){
        for(let i = 0; i < n; i++){
            let temp = 0;
            for(let j = 1; j <= k; j++){
                temp += code[(i + j) % n];
            }
            df[i] = temp;
        }
    }else if(k < 0){
        for(let i = 0; i < n; i++){
            let temp = 0;
            for(let j = 1; j <= k * -1; j++){
                temp += code[(i - j + n) % n];
            }
            df[i] = temp;
        }
    }

    return df;
};
