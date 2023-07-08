var flat = function (arr, n) {
    if(n === 0)
        return arr;

    let ans = [];
    arr.forEach((e) => {
        if(0 < n && Array.isArray(e))
            ans.push(...flat(e, n - 1));
        else
            ans.push(e);
    })

    return ans;
};
