var maximumGroups = function(grades) {
    let max = 0;
    let total = 0;

    while(max + total + 1 <= grades.length){
        max++;
        total += max;
    }

    return max;
};
