var mySqrt = function(x) {
    let root = x;
    
    while(x < root * root){
        root = ((root + x / root) / 2) | 0;
    }

    return root;
};
