var spiralOrder = function(matrix) {
    let top = 0;
    let bot = matrix.length - 1;
    let left = 0;
    let right = matrix[0].length - 1;
    let spiral = [];

    // Find all the elements of the matrix in spiral order
    while(top <= bot && left <= right){
        // Top row
        for(let i = left; i <= right; i++)
            spiral.push(matrix[top][i]);
        top++;

        // Right column
        for(let i = top; i <= bot; i++)
            spiral.push(matrix[i][right]);
        right--;

        // Bottom row
        if(top <= bot){
            for(let i = right; left <= i; i--)
                spiral.push(matrix[bot][i]);
            bot--;
        }

        // Left column
        if(left <= right){
            for(let i = bot; top <= i; i--)
                spiral.push(matrix[i][left]);
            left++;
        }
    }

    return spiral;
};
