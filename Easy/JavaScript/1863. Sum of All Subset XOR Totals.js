var subsetXORSum = function(nums) {
    return subsetXORSumHelper(nums, 0, 0);
};

var subsetXORSumHelper = function(nums, i, j){
    if(i == nums.length)
        return j;
    return subsetXORSumHelper(nums, i + 1, j^nums[i]) + subsetXORSumHelper(nums, i + 1, j);
};
