var countGoodRectangles = function(rectangles) {
    let len = 0;
    let count = 0;

    rectangles.forEach(rect =>{
        len = Math.max(len, Math.min(rect[0], rect[1]));
    })

    rectangles.forEach(rect =>{
        if(Math.min(rect[0], rect[1]) == len)
            count++;
    })

    return count;
};
