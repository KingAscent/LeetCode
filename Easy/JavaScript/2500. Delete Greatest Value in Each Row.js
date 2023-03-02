var deleteGreatestValue = function(grid) {
    let sum = 0;

    grid.forEach((i) => {
        i.sort((a, b) => a - b);
    });

    for(let i = 0; i < grid[0].length; i++){
        let max = 0;
        grid.forEach((e) => {
            if(max <= e[i])
                max = e[i];
        });
        sum += max;
    };

    return sum;
};
