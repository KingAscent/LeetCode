var oddCells = function(m, n, indices) {
    let row = new Array(m).fill(0);
    let col = new Array(n).fill(0);

    for(let i = 0; i < indices.length; i++){
        row[indices[i][0]]++;
        col[indices[i][1]]++;
    }

    let oddRows = 0;
    for(let i = 0; i < m; i++){
        if(row[i] % 2 == 1)
            oddRows++;
    }

    let oddCols = 0;
    for(let i = 0; i < n; i++){
        if(col[i] % 2 == 1)
            oddCols++;
    }

    return (oddRows * n) + (oddCols * m) - (2 * oddRows * oddCols);
};
