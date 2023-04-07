var distributeCandies = function(candyType) {
    candyType.sort((a, b) => a - b);
    let len = candyType.length;
    let count = 0;
    let limit = len / 2;

    for(let i = 0; i < len && 0 < limit; i++){
        while(i < len - 1 && candyType[i] == candyType[i + 1]){
            i++;
        }
        count++;
        limit--;
    }

    return count;
};
