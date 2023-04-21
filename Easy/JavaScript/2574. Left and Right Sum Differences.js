var leftRigthDifference = function(nums) {
    let left = 0;
    let right = 0;

    nums.forEach((n) => {
        right += n;
    })

    for(let i = 0; i < nums.length; i++){
        left += nums[i];
        right -= nums[i];
        nums[i] = Math.abs((left - nums[i]) - right);
    }

    return nums;
};
