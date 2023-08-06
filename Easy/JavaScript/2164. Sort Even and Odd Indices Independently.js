var sortEvenOdd = function(nums) {
    // Evens
    for(let i = 0; i < nums.length; i += 2){
        for(let j = i + 2; j < nums.length; j += 2){
            if(nums[j] <= nums[i]){
                let temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }

    // Odds
    for(let i = 1; i < nums.length; i += 2){
        for(let j = i + 2; j < nums.length; j += 2){
            if(nums[i] <= nums[j]){
                let temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }

    return nums;
};
