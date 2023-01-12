var trimMean = function(arr) {
    let sum = 0;
    let fivePercent = arr.length / 20;
    arr.sort((a, b) => a - b);

    for(let i = fivePercent; i < arr.length - fivePercent; i++){
        sum += arr[i];
    }

    return (sum * 1.0) / (arr.length - (2 * fivePercent));
};
