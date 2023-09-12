var passThePillow = function(n, time) {
    let place = 0;
    let direction = Math.floor(time / (n - 1));
    let remainder = Math.floor(time % (n - 1));

    if(Math.floor(direction % 2) == 0)
        place = remainder + 1;
    else
        place = n - remainder;
    
    return place;
};
