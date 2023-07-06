var minSubArrayLen = function(target, nums) {
    let n = nums.length;
    let minLen = n + 1;
    let j = 0;
    let sum = 0;

    for(let i = 0; i < n; i++){
        sum += nums[i];
        while(target <= sum){
            let currLen = i - j + 1;
            minLen = Math.min(minLen, currLen);
            sum -= nums[j];
            j++;
        }
    }

    if(minLen != n + 1)
        return minLen;
    else
        return 0;
};
