var countDistinctIntegers = function(nums) {
    // Initialize a set to keep track of each individual num
    // Sets do not allow duplicate elements so simialr numbers are ignored
    let numbers = new Set();

    // For each number in nums, first add the number
    // The reverse the number and add it to the set
    nums.forEach((n) => {
        numbers.add(n);
        let numR = 0; // Variable for the number reversed
        while(n != 0){
            // Evaluate each number in reverse order
            numR = numR * 10 + (n % 10);
            n = Math.floor(n / 10);
        }
        numbers.add(numR);
    });

    // Return the size of the set
    return numbers.size;
};
