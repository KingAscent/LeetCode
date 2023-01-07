var smallestRangeI = function(nums, k) {
    nums.sort(sortNums);
    if(nums.length == 1 || nums[nums.length - 1] - k <= nums[0] + k)
        return 0;
    
    return nums[nums.length - 1] - nums[0] - k * 2;
};

function sortNums(a, b){
    return a - b;
}
