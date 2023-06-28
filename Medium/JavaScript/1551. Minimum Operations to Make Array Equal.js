var minOperations = function(n) {
    let count = 0;

    for(let i = (2 * n - 2) / 2; 0 <= i; i -= 2)
        count += i;

    return count;
};
