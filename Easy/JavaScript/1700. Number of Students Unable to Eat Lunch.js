var countStudents = function(students, sandwiches) {
    let zeros = 0;
    let ones = 0;

    for(let n of students){
        if(n == 0)
            zeros++;
        else
            ones++;
    }

    for(let n of sandwiches){
        if((n == 0 && zeros == 0) || (n == 1 && ones == 0))
            break;
        if(n == 0)
            zeros--;
        else
            ones--;
    }

    return Math.max(zeros, ones);
};
