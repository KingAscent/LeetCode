var countPoints = function(rings) {
    let count = 0;
    let red = Array(10).fill(0);
    let blue = Array(10).fill(0);
    let green = Array(10).fill(0);

    // Even position of rings
    for(let i = 0; i < rings.length; i += 2){
        let c = rings.charAt(i);
        let index = rings.charAt(i + 1) - '0';
        if(c == 'R')
            red[index]++;
        if(c == 'B')
            blue[index]++;
        if(c == 'G')
            green[index]++;
    }

    // Odd position of rings
    for(let i = 0; i < 10; i++){
        if(red[i] != 0 && blue[i] != 0 && green[i] != 0)
            count++;
    }

    return count;
};
