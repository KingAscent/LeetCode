var smallestDistancePair = function(nums, k) {
    // Sort the array, then initialize a min and max variable
    nums.sort((a, b) => a - b);
    let min = 0;
    let max = nums[nums.length - 1] - nums[0];

    // Binary search algorithm
    while(min < max){
        let mid = Math.floor((min + max) / 2);
        let count = 0;
        let i = 0;

        // Find pairs with distance less than or equal to middle
        for(let j = 0; j < nums.length; j++){
            // Run through this segment of code once, then break
            while(true){
                let diff = nums[j] - nums[i];
                if(mid < diff)
                    i++;
                else
                    break;
            }
            count += j - i;
        }

        if(k <= count)
            max = mid;
        else
            min = mid + 1;
    }

    // Return the smallest distance found
    return min;
};
