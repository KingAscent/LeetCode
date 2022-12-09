var maxProductDifference = function(nums) {
    nums.sort((a, b) => a - b);
    const len = nums.length - 1;
    return (nums[len] * nums[len - 1]) - (nums[0] * nums[1]);
};
