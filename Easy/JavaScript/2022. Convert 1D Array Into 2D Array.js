var construct2DArray = function(original, m, n) {
    if(original.length != m * n)
        return Array(0);
    
    let arr = Array(m);
    for(let i = 0; i < arr.length; i++){
        arr[i] = Array(n);
    }

    let row = 0;
    let col = 0;

    original.forEach(num => {
        arr[row][col] = num;
        col++;
        if(col == n){
            col = 0;
            row++;
        }
    })

    return arr;
};
