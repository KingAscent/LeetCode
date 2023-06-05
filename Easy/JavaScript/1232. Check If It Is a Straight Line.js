var checkStraightLine = function(coordinates) {
    let x1 = coordinates[0][0];
    let y1 = coordinates[0][1];
    let x2 = coordinates[1][0];
    let y2 = coordinates[1][1];

    for(let i = 2; i < coordinates.length; i++){
        let x = coordinates[i][0];
        let y = coordinates[i][1];

        if((y - y1) * (x - x2) != (y - y2) * (x - x1))
            return false;
    }

    return true;
};
