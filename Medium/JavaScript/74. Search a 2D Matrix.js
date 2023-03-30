var searchMatrix = function(matrix, target) {
    let r = matrix.length;
    let c = matrix[0].length;
    let i = 0;
    let j = c - 1;

    while(0 <= i && i < r && 0 <= j && j < c){
        if(matrix[i][j] == target)
            return true;
        else if(target < matrix[i][j])
            j--;
        else
            i++;
    }

    return false;
};
