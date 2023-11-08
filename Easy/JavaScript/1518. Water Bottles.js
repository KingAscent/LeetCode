var numWaterBottles = function(numBottles, numExchange) {
    let count = numBottles;

    while(numExchange <= numBottles){
        let temp = Math.floor(numBottles / numExchange);
        count += temp;
        numBottles = temp + (numBottles - (numExchange * temp));
    }

    return count;
};
