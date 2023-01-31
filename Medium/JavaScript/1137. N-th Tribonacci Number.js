var tribonacci = function(n) {
    // Restrictions of n
    if(n < 3){
        if(n == 2)
            return 1;
        return n;
    }

    // Initialize array to contain all the values of the Tribonacci sequence
    let tri = new Array(n + 1);
    tri[0] = 0;
    tri[1] = 1;
    tri[2] = 1;

    // Calculate the nth value of the Tribonacci sequence by filling the array
    for(let i = 3; i <= n; i++){
        tri[i] = tri[i - 1] + tri[i - 2] + tri[i - 3];
    }

    // Return the nth value of the Tribonacci sequence
    return tri[n];
};
