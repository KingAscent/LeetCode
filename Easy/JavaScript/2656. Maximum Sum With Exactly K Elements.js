var maximizeSum = function(nums, k) {
    let count = 0;
    let max = 0;

    for(let i = 0; i < nums.length; i++){
        max = Math.max(max, nums[i]);
    }

    while(0 < k){
        count += max;
        max++;
        k--;
    }

    return count;
};
