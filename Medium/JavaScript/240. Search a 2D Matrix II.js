var searchMatrix = function(matrix, target) {
    let row = matrix.length;
    let col = matrix[0].length;
    let i = 0;
    let j = col - 1;

    while(i < row && 0 <= j){
        if(matrix[i][j] == target)
            return true;
        else if(target < matrix[i][j])
            j--;
        else
            i++;
    }

    return false;
};
