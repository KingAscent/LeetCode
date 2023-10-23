var findPoisonedDuration = function(timeSeries, duration) {
    let sec = duration;

    for(let i = 1; i < timeSeries.length; i++){
        sec += Math.min(duration, timeSeries[i] - timeSeries[i - 1]);
    }

    return sec;
};
