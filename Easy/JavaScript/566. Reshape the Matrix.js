var matrixReshape = function(mat, r, c) {
    let m = mat.length;
    let n = mat[0].length;
    if(r * c != m * n)
        return mat;
    
    let rs = Array(r).fill(0);
    for(let i = 0; i < r; i++){
        rs[i] = Array(c).fill(0);
    }
    for(let i = 0; i < r * c; i++){
        rs[Math.floor(i / c)][i % c] = mat[Math.floor(i / n)][i % n];
    }

    return rs;
};
