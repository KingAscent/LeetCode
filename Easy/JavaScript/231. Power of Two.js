var isPowerOfTwo = function(n) {
    return 0 < n && (n & n - 1) == 0;
};
