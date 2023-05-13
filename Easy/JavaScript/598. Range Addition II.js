var maxCount = function(m, n, ops) {
    let r = m;
    let c = n;

    ops.forEach((i) => {
        r = Math.min(r, i[0]);
        c = Math.min(c, i[1]);
    })

    return r * c;
};
