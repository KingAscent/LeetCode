var sumOddLengthSubarrays = function(arr) {
    let sum = 0;

    // Count each element in an odd-length sub-array and multiply
    // the array elements to get the output of the sum
    for(let i = 0; i < arr.length; i++){
        let present = Math.floor(((i + 1) * (arr.length - i) + 1) / 2);
        sum += present * arr[i];
    }

    return sum;
};
