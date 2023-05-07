var largestTriangleArea = function(points) {
    let n = points.length;
    let largest = 0;

    for(let i = 0; i < n; i++){
        for(let j = i + 1; j < n; j++){
            for(let k = j + 1; k < n; k++){
                let temp = 0;
                let a = points[i];
                let b = points[j];
                let c = points[k];
                temp = Math.abs(area(a, b) + area(b, c) + area(c, a));
                largest = Math.max(largest, temp);
            }
        }
    }

    return largest;
};

var area = function(a, b) {
    let base = b[0] - a[0];
    let height = a[1] + b[1];
    return 0.5 * base * height;
}
