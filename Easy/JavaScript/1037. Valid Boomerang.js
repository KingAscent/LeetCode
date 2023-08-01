var isBoomerang = function(points) {
    let x1 = points[0][0];
    let x2 = points[1][0];
    let x3 = points[2][0];
    let y1 = points[0][1];
    let y2 = points[1][1];
    let y3 = points[2][1];

    return (x3 - x2) * (y2 - y1) != (x2 - x1) * (y3 - y2);
};
