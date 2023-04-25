var minOperations = function(nums) {
    let count = 0;
    let prev = 0;

    for(let n of nums){
        if(n <= prev){
            count += prev + 1 - n;
            prev++;
        }else{
            prev = n;
        }
    }

    return count;
};
