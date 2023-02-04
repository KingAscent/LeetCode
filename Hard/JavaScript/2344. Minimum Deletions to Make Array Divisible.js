var minOperations = function(nums, numsDivide) {
    // Initialize a greatest common divisor and a temp value
    let gcd = numsDivide[0];
    let temp = 0;

    // Find the greatest common divisor of numsDivide
    numsDivide.forEach((i) => {
        while(0 < i){
            temp = gcd % i;
            gcd = i;
            i = temp;
        }
    })

    // Sort the nums array, then ignore any elements in nums that
    // are smaller than gcd. Return the smallest element nums[i]
    // that divides gcd
    nums.sort((a, b) => a - b);
    for(let i = 0; i < nums.length && nums[i] <= gcd; i++){
        if(gcd % nums[i] === 0)
            return i;
    }

    // No such element exists in nums, return -1
    return -1;
};
