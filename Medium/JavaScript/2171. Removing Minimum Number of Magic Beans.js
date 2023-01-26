var minimumRemoval = function(beans) {
    // Initialize values to store max and sum
    // Then stort the array
    let max = 0;
    let sum = 0;
    beans.sort((a, b) => a - b);

    // Use a for loop to remove the beans from the bags with
    // the least amount of beans in them until each non-empty
    // bag has the same amount of beans
    for(let i = 0; i < beans.length; i++){
        sum += beans[i];
        max = Math.max(max, beans[i] * (beans.length - i));
    }

    // Return the amount of beans that had to be removed
    return sum - max;
};
