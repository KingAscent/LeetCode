var largestAltitude = function(gain) {
    let high = 0;
    let point = 0;

    for(let i = 0; i < gain.length; i++){
        point += gain[i];
        high = Math.max(high, point);
    }

    return high;
};
