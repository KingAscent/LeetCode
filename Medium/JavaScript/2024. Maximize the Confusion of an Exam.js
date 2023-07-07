var maxConsecutiveAnswers = function(answerKey, k) {
    let fs = 0;
    let ts = 0;
    let ansKey = 0;
    let start = 0;
    let end = 0;

    while(end < answerKey.length){
        if(answerKey.charAt(end) == 'F')
            fs++;
        else
            ts++;
        while(k < Math.min(fs, ts)){
            if(answerKey.charAt(start) == 'F')
                fs--;
            else
                ts--;
            start++;
        }
        ansKey = Math.max(ansKey, fs + ts);
        end++;
    }

    return ansKey;
};
