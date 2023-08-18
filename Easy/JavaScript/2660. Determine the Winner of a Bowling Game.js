var isWinner = function(player1, player2) {
    let p1 = 0;
    let p2 = 0;

    for(let i = 0; i < player1.length; i++){
        if((i == 1 && player1[i - 1] == 10) ||
            (2 <= i && (player1[i - 1] == 10 || player1[i - 2] == 10)))
            p1 += player1[i];

        if((i == 1 && player2[i - 1] == 10) ||
            (2 <= i && (player2[i - 1] == 10 || player2[i - 2] == 10)))
            p2 += player2[i];

        p1 += player1[i];
        p2 += player2[i];
    }

    return p2 < p1 ? 1 : p1 < p2 ? 2 : 0;
};
