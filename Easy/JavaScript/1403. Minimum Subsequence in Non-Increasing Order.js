var minSubsequence = function(nums) {
    let n = nums.length;
    let sum = 0;
    let total = 0;
    let ans = [];
    nums.sort((a, b) => a - b);

    for(let i = 0; i < n; i++){
        total += nums[i];
    }

    for(let i = n - 1; 0 <= i; i--){
        ans.push(nums[i]);
        sum += nums[i];
        if(total - sum < sum)
            break;
    }
    
    return ans;
};
