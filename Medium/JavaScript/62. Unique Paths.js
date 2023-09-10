var uniquePaths = function(m, n) {
    let row = Array(n).fill(1);

    for(let i = 1; i < m; i++){
        let currRow = Array(n).fill(1);
        for(let j = 1; j < n; j++){
            currRow[j] = currRow[j - 1] + row[j];
        }
        row = currRow;
    }

    return row[n - 1];
};
