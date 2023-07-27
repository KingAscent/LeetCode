var maxRunTime = function(n, batteries) {
    batteries.sort((a, b) => a - b);
    let charge = batteries.slice(-n);
    let extra = batteries.slice(0, -n).reduce((acc, val) => acc + val, 0);

    for(let i = 0; i < n - 1; i++){
        if(extra / (i + 1) < charge[i + 1] - charge[i])
            return charge[i] + Math.floor(extra / (i + 1));
        extra -= (i + 1) * (charge[i + 1] - charge[i]);
    }

    return charge[charge.length - 1] + Math.floor(extra / n);
};
