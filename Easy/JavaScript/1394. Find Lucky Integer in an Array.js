var findLucky = function(arr) {
    arr.sort((a, b) => a - b);
    let count = Array(arr[arr.length - 1] + 1).fill(0);
    let largest = -1;

    for(let n of arr)
        count[n]++;
    for(let i = 1; i < count.length; i++){
        if(count[i] == i)
            largest = i;
    }

    return largest;
};
