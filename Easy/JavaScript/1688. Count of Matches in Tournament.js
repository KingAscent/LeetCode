var numberOfMatches = function(n) {
    // Base case
    if(n <= 2)
        return Math.floor(n / 2);
    
    // Recursive cases
    if(n % 2 == 0)
        return (n / 2) + numberOfMatches(n / 2);
    else
        return ((n - 1) / 2) + numberOfMatches((n - 1) / 2 + 1);
};
