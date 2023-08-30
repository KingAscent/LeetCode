var captureForts = function(forts) {
    let sum = 0;
    let count = 0;
    let max = 0;

    for(let i = 0; i < forts.length; i++){
        if(forts[i] != 0){
            sum += forts[i];
            if(sum == 0)
                max = Math.max(max, count);
            sum = forts[i];
            count = 0;
        }else if(sum != 0)
            count++;
    }

    return max;
};
