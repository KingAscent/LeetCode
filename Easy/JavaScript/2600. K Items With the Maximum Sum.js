var kItemsWithMaximumSum = function(numOnes, numZeros, numNegOnes, k) {
    return Math.min(k, numOnes) - Math.max(0, k - numOnes - numZeros);
};
