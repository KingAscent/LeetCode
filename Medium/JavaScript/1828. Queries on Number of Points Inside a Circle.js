var countPoints = function(points, queries) {
    let nums = Array(queries.length).fill(0);
    let i = 0;

    queries.forEach(q => {
        let x0 = q[0];
        let y0 = q[1];
        let r = q[2];
        points.forEach(p => {
            let x = p[0];
            let y = p[1];
            let dx = x - x0;
            let dy = y - y0;
            if((dx * dx) + (dy * dy) <= (r * r))
                nums[i]++;
        })
        i++;
    })

    return nums;
};
