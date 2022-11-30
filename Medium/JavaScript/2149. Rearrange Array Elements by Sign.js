var rearrangeArray = function(nums) {
    // Create a new array, an even index, and an odd index variable
    let rearranged = new Array(nums.length);
    let i = 0;
    let j = 1;

    // Go over the array adding positives, then negatives, to the array
    for(let k = 0; k < nums.length; k++){
        if(0 < nums[k]){
            rearranged[i] = nums[k];
            i += 2;
        }else{
            rearranged[j] = nums[k];
            j += 2;
        }
    }

    // Return the new array
    return rearranged;
};
