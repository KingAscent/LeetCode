var map = function(arr, fn) {
    let tArr = [];

    for(let i = 0; i < arr.length; i++){
        let temp = fn(arr[i], i);
        tArr.push(temp);
    }

    return tArr;
};
