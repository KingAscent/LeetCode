var maxPoints = function(points) {
    let count = 2; // Initialize count at 2 since every line needs at least 2 points
    let n = points.length;
    if(n <= 2)
        return n;
    
    for(let i = 0; i < n; i++){
        for(let j = i + 1; j < n; j++){
            let temp = 2; // Initialize temp count at 2 since every line needs at least 2 points

            /*
                See if a point k is the line that has a slope of (y2 - y1)/(x2 - x1)
                This can be expressed with (ky - y1)/(kx - x1) == (y2 - ky) / (x2 - kx)
                And rewritten as (ky - y1)(x2 - kx) == (y2 - ky)(kx - x1)
            */
            for(let k = 0; k < n; k++){
                if(k != i && k != j){
                    let a = points[j][1] - points[i][1]; // ky - y1
                    let b = points[i][0] - points[k][0]; // x2 - kx
                    let c = points[i][1] - points[k][1]; // y2 - ky
                    let d = points[j][0] - points[i][0]; // kx - x1
                    if(a * b == c * d)
                        temp++;
                }
            }
            count = Math.max(count, temp);
        }
    }

    return count;
};
