var sumZero = function(n) {
    const myArray = new Array(n);
    var sum = 0;

    for(let i = 1; i < n; i++){
        sum += i;
        myArray[i] = i;
    }

    myArray[0] =- sum;

    return myArray;
};
