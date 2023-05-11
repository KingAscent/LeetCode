var rowAndMaximumOnes = function(mat) {
    let row = 0;
    let count = 0;

    for(let i = 0; i < mat.length; i++){
        let temp = 0;
        for(let j = 0; j < mat[0].length; j++){
            if(mat[i][j] == 1)
                temp++;
        }
        if(count < temp){
            row = i;
            count = temp;
        }
    }

    return [row, count];
};
