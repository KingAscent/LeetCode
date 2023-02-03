var convert = function(s, numRows) {
    // Filter out strings on a singular row
    if(numRows == 1)
        return s;
    
    // Initialize a variable to contain the new string, the string length,
    // and a variable that has the step for each character's indentation
    let zigZag = "";
    const len = s.length;
    const step = 2 * (numRows - 1);

    // Use a for loop to design each row
    for(let i = 0; i < numRows; i++){
        //Use a for loop to place each character into the row
        for(let j = i; j < len; j += step){
            zigZag += s.charAt(j);
            if(i != 0 && i != (step / 2) && (j + step - 2 * i) < len)
                zigZag += s.charAt(j + step - 2 * i);
        }
    }

    // Return the zigzag string
    return zigZag;
};
