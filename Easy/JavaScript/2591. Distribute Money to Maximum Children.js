var distMoney = function(money, children) {
    if(money < children)
        return -1;
    money -= children;

    let count = 0;
    while(7 <= money && count != children){
        money -= 7;
        count++;
    }

    if(money != 0 && ((count == children) || (money == 3 && children - count == 1)))
        count--;
    
    return count;
};
