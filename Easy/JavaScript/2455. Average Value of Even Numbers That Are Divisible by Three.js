var averageValue = function(nums) {
    let count = 0;
    let avg = 0;

    for(let n of nums){
        if(Math.floor(n % 6) == 0){
            avg += n;
            count++;
        }
    }

    return avg == 0 ? 0 : Math.floor(avg / count);
};
