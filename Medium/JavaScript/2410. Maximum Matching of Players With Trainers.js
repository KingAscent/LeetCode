var matchPlayersAndTrainers = function(players, trainers) {
    players.sort((a, b) => a - b);
    trainers.sort((a, b) => a - b);
    let i = 0;
    let j = 0;
    let count = 0;

    while(i < players.length && j < trainers.length){
        if(players[i] <= trainers[j]){
            i++;
            count++;
        }
        j++;
    }

    return count;
};
