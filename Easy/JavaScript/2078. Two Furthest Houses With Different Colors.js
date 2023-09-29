var maxDistance = function(colors) {
    let n = colors.length;
    let i = 0;
    let j = n - 1;

    while(colors[0] == colors[j])
        j--;
    while(colors[n - 1] == colors[i])
        i++;
    
    return Math.max(j, n - i - 1);
};
