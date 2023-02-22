var shipWithinDays = function(weights, days) {
    let start = 0;
    let end = 0;

    weights.forEach(i => {
        start = Math.max(start, i);
        end += i;
    });

    while(start <= end){
        let mid = start + Math.floor((end - start) / 2);
        let cap = findDay(weights, mid);
        if(cap <= days)
            end = mid - 1;
        else
            start = mid + 1;
    }

    return start;
};

function findDay(weights, mid){
    let date = 0;
    let sum = 0;

    for(let i = 0; i < weights.length; i++){
        if(sum + weights[i] <= mid){
            sum += weights[i];
        }else{
            sum = weights[i];
            date++;
        }
    }

    return date + 1;
};
