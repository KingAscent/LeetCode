var minDeletionSize = function(strs) {
    let row = strs.length;
    let col = strs[0].length;
    let count = 0;

    for(let i = 0; i < col; i++){
        for(let j = 0; j < row - 1; j++){
            if(strs[j].charAt(i) > strs[j + 1].charAt(i)){
                count++;
                break;
            }
        }
    }

    return count;
};
