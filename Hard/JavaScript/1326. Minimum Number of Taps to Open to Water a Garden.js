var minTaps = function(n, ranges) {
    let range = Array(n + 1).fill(0);

    for(let i = 0; i < ranges.length; i++){
        let left = Math.max(0, i - ranges[i]);
        let right = Math.min(n, i + ranges[i]);
        range[left] = Math.max(range[left], right);
    }

    let end = 0;
    let maxRange = 0;
    let taps = 0;
    let i = 0;

    while(end < n){
        while(i <= end){
            maxRange = Math.max(maxRange, range[i]);
            i++;
        }

        if(maxRange <= end)
            return -1; // Can't water the garden
        end = maxRange;
        taps++;
    }

    return taps;
};
