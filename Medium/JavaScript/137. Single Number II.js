var singleNumber = function(nums) {
    // Filter out arrays of length 1
    if(nums.length == 1)
        return nums[0];
    
    // Sort the array and find the integer that does not match
    // the integers to the left and right of it
    nums.sort();
    if(nums[0] != nums[1]) // If the 1st integer does not match the 2nd
        return nums[0];
    for(let i = 1; i < nums.length - 1; i++){
        if(nums[i] != nums[i - 1] && nums[i] != nums[i + 1])
            return nums[i];
    }

    // Return the last number in the array
    return nums[nums.length - 1];
};
