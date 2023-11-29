var convertToBase7 = function(num) {
    if(num == 0)
        return "0";

    let neg = 0 <= num ? "" : "-";
    base7 = "";
    num = Math.abs(num);

    while(1 <= num){
        base7 = (num % 7).toString() + base7;
        num = Math.floor(num / 7);
    }
    
    return neg + base7;
};
