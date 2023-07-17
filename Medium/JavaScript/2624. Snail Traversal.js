Array.prototype.snail = function(rowsCount, colsCount) {
    if(rowsCount * colsCount !== this.length)
        return [];

    let res = Array(rowsCount).fill().map(() => []);
    for(let i = 0; i < this.length; i++){
        let j = Math.floor(i / rowsCount);
        let temp = i % rowsCount;
        if(j % 2 === 0)
            res[temp][j] = this[i];
        else
            res[rowsCount - temp - 1][j] = this[i];
    }

    return res;
}
