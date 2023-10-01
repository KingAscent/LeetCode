var integerReplacement = function(n) {
    let count = checkCount(n);

    return count;
};

var checkCount = function(n) {
    if(n == 1)
        return 0;
    else if(n % 2 == 0)
        return 1 + checkCount(n / 2);
    else
        return 1 + Math.min(checkCount(n + 1), checkCount(n - 1));
}
