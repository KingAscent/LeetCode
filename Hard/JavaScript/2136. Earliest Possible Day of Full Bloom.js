var earliestFullBloom = function(plantTime, growTime) {
    let max = 0;
    growTime.forEach((i) => {
        max = Math.max(max, i);
    })

    let arr = Array(max + 1).fill(0);
    let temp = 0;
    let min = 0;

    for(let i = 0; i < plantTime.length; i++){
        arr[growTime[i]] += plantTime[i];
    }

    for(let i = max; 0 < i; i--){
        if(arr[i] != 0){
            temp += arr[i];
            min = Math.max(min, temp + i);
        }
    }

    return min;
};
