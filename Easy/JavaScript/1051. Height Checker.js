var heightChecker = function(heights) {
    let sorted = [];
    for(let i = 0; i < heights.length; i++){
        sorted.push(heights[i]);
    }
    let count = 0;

    sorted.sort((a, b) => a - b);
    for(let i = 0; i < heights.length; i++){
        if(heights[i] != sorted[i])
            count++;
    }

    return count;
};
