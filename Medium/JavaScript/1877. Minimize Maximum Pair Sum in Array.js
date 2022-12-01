var minPairSum = function(nums) {
    // Sort the array, initialize an index for a new array, initialize new array
    nums.sort((a, b) => a-b);
    let index = 0;
    let pairs = [nums.length / 2];

    // Use a for loop to travel over nums, placing each pair
    // Increase the index value after each pair is added
    for(let i = 0; i < nums.length / 2; i++){
        pairs[index] = nums[i] + nums[nums.length - i - 1];
        index++;
    }

    // Return the max in pairs
    return Math.max(...pairs);
};
