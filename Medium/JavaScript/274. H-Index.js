var hIndex = function(citations) {
    let len = citations.length;
    let arr = Array(len + 1).fill(0);

    citations.forEach(num => {
        if(len <= num)
            arr[len]++;
        else
            arr[num]++;
    })

    let count = 0;
    for(let i = len; 0 <= i; i--){
        count += arr[i];
        if(i <= count)
            return i;
    }

    return 0;
};
