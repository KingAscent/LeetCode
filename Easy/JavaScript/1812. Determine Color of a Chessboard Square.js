var squareIsWhite = function(coordinates) {
    return coordinates[0].charCodeAt(0) % 2 !== parseInt(coordinates[1]) % 2;
};
