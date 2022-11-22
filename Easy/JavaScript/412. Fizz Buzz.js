var fizzBuzz = function(n) {
    const myList = [];

    for(let i = 1; i <= n; i++){
        if(i % 15 == 0){
            myList[i - 1] = "FizzBuzz";
        }else if(i % 3 == 0){
            myList[i - 1] = "Fizz";
        }else if(i % 5 == 0){
            myList[i - 1] = "Buzz";
        }else{
            myList[i - 1] = "" + i;
        }
    }

    return myList;
};
