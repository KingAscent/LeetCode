var maximumProduct = function(nums) {
    nums.sort((a, b) => a - b);
    let twoNegatives = nums[0] * nums[1] * nums[nums.length - 1];
    let noNegatives = nums[nums.length - 1] * nums[nums.length - 2] * nums[nums.length - 3];
    return Math.max(noNegatives, twoNegatives);
};
