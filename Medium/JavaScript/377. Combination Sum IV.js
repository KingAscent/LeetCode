var combinationSum4 = function(nums, target) {
    let cases = Array(target + 1).fill(0);
    cases[0] = 1;

    for(let i = 1; i <= target; i++){
        for(let n of nums){
            if(n <= i)
                cases[i] += cases[i - n];
        }
    }

    return cases[target];
};
