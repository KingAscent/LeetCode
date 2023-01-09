var countNegatives = function(grid) {
    let count = 0;

    grid.forEach(i => {
        i.forEach(j => {
            if(j < 0)
                count++;
        })
    })

    return count;
};
