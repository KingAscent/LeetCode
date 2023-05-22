var countTriplets = function(arr) {
    let count = 0;

    for(let i = 0; i < arr.length; i++){
        let temp = arr[i];
        for(let j = i + 1; j < arr.length; j++){
            // xor of element
            temp ^= arr[j];
            if(temp == 0)
                count += j - i;
        }
    }

    return count;
};
