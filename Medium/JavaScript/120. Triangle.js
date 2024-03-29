var minimumTotal = function(triangle) {
    for(let i = triangle.length - 2; 0 <= i; i--){
        for(let j = triangle[i].length - 1; 0 <= j; j--){
            triangle[i][j] += Math.min(triangle[i + 1][j], triangle[i + 1][j + 1]);
        }
    }

    return triangle[0][0];
};
