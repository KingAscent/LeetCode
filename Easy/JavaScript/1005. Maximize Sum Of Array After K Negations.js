var largestSumAfterKNegations = function(nums, k) {
    nums.sort((a, b) => a - b);
    let n = nums.length;

    for(let i = 0; i < n; i++){
        if(k != 0 && nums[i] < 0){
            nums[i] *= -1;
            k--;
        }else{
            break;
        }
    }

    if(k != 0){
        nums.sort((a, b) => a - b);
        while(k != 0){
            nums[0] *= -1;
            k--;
        }
    }

    let sum = 0;
    for(let i = 0; i < n; i++){
        sum += nums[i];
    }

    return sum;
};
