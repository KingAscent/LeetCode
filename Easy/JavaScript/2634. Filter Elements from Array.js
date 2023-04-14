var filter = function(arr, fn) {
    let filter = [];

    arr.forEach((x, i) => {
        if(fn(x, i))
            filter.push(x);
    })

    return filter;
};
