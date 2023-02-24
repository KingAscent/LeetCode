var solution = function(isBadVersion) {
    return function(n) {
        let first = 0;
        let last = n;
        let ver = 0;

        while(first <= last){
            let temp = first + Math.floor((last - first) / 2);
            if(isBadVersion(temp)){
                ver = temp;
                last = temp - 1;
            }
            else{
                first = temp + 1;
            }
        }
        
        return ver;
    };
};
