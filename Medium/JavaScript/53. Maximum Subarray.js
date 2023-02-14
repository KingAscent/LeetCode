var maxSubArray = function(nums) {
    // Initialize 2 variables to keep track of the sum
    let sum = nums[0];
    let tempSum = sum;

    // Use a for loop to see what the largest subarray is
    for(let i = 1; i < nums.length; i++){
        tempSum = Math.max(tempSum + nums[i], nums[i]);
        sum = Math.max(tempSum, sum);
    }

    // Return the largest subarray sum
    return sum;
};
