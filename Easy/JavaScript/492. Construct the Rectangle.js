var constructRectangle = function(area) {
    let w = Math.floor(Math.sqrt(area));

    while(Math.floor(area % w) != 0)
        w--;

    return [area / w, w];
};
