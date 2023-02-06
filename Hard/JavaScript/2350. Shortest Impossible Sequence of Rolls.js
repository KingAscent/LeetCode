var shortestSequence = function(rolls, k) {
    // Initialize a variable and a set to keep track of the length
    // of the shortest sequence
    let seq = 1;
    let set = new Set();

    // Find each complete sequence
    rolls.forEach((i) =>{
        set.add(i);
        if(set.size == k){
            seq++;
            set.clear();
        }
    })

    // Return the length of the shortest sequence
    return seq;
};
