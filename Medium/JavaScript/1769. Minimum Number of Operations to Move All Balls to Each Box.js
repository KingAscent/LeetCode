var minOperations = function(boxes) {
    // Initialize an array to contain the number of
    // operations
    ops = Array(boxes.length).fill(0);

    // Use a for loop to move all the balls to the ith box
    for(let i = 0; i < boxes.length; i++){
        let cost = 0;
        for(let j = 0; j < boxes.length; j++){
            if(boxes.charAt(j) == '1')
                cost += Math.abs(i - j);
        }
        ops[i] = cost;
    }

    // Return the ops array
    return ops;
};
