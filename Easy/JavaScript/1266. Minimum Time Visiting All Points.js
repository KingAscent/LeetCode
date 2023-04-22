var minTimeToVisitAllPoints = function(points) {
    let xInt = points[0][0];
    let yInt = points[0][1];
    let sec = 0;

    for(let i = 0; i < points.length; i++){
        let x = points[i][0];
        let y = points[i][1];
        let dx = Math.abs(x - xInt);
        let dy = Math.abs(y - yInt);
        let temp = Math.max(dx, dy);
        dx -= temp;
        dy -= temp;
        sec += temp + Math.max(0, dx) + Math.max(0, dy);
        xInt = x;
        yInt = y;
    }

    return sec;
};
