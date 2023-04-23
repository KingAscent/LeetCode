var decode = function(encoded, first) {
    let original = Array(encoded.length + 1);
    original[0] = first;

    for(let i = 0; i < encoded.length; i++){
        original[i + 1] = original[i] ^ encoded[i];
    }

    return original;
};
