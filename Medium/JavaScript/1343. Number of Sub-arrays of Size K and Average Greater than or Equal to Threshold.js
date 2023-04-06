var numOfSubarrays = function(arr, k, threshold) {
    let count = 0;
    let sum = 0;
    let avg = 0;

    for(let i = 0; i < arr.length; i++){
        sum += arr[i];
        if(k - 1 <= i){
            avg = sum / k;
            if(threshold <= avg)
                count++;
            sum -= arr[i - (k - 1)];
        }
    }

    return count;
};
