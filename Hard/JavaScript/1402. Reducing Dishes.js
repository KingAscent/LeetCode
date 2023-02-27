var maxSatisfaction = function(satisfaction) {
    satisfaction.sort((a, b) => a - b);
    let n = satisfaction.length;
    let sums = Array(n + 1).fill(0);
    let score = 0;
    let maxScore = 0;

    // Use a for loop to calculate the sums from right to left
    for(let i = (n - 1); 0 <= i; i--){
        sums[i] = sums[i + 1] + satisfaction[i];
        score += (i + 1) * satisfaction[i];
    }

    if(0 < score)
        maxScore = score;
    
    for(let i = 0; i < n; i++){
        score -= satisfaction[i];
        score -= sums[i + 1];
        if(maxScore < score)
            maxScore = score;
    }

    return maxScore;
};
