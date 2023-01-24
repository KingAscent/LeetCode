var canJump = function(nums) {
    // Initialize a jump value
    let jump = 0;

    // Use a for loop to check how far each index allows us to jump
    // And see if we are able to jump over each zero
    for(let i = 0; i < nums.length; i++){
        if(jump < i)
            // We cannot jump over the zero, return false
            return false;
        jump = Math.max(jump, i + nums[i]);
    }

    // All zeros are able to be jumped over
    return true;
};
