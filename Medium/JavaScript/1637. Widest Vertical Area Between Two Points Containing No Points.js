var maxWidthOfVerticalArea = function(points) {
    let width = 0;
    let x = Array(points.length);

    for(let i = 0; i < points.length; i++){
        x[i] = points[i][0];
    }
    x.sort((a, b) => a - b);
    for(let i = 0; i < x.length - 1; i++){
        width = Math.max(width, (x[i + 1] - x[i]));
    }

    return width;
};
