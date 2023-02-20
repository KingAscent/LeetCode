var numTeams = function(rating) {
    let count = 0;

    for(let i = 0; i < rating.length; i++){
        let left = 0;
        let right = 0;
        for(let j = 0; j < i; j++){
            if(rating[j] < rating[i])
                left++;
        }
        for(let k = i + 1; k < rating.length; k++){
            if(rating[i] < rating[k])
                right++;
        }
        count += (left * right) + (i - left) * (rating.length - i - right - 1);
    }

    return count;
};
