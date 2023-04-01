var romanToInt = function(s) {
    let num = 0;
    let ans = 0;

    for(let i = s.length - 1; 0 <= i; i--){
        switch(s.charAt(i)){
            case 'I' : num = 1;
                break;
            case 'V' : num = 5;
                break;
            case 'X' : num = 10;
                break;
            case 'L' : num = 50;
                break;
            case 'C' : num = 100;
                break;
            case 'D' : num = 500;
                break;
            case 'M' : num = 1000;
                break;
        }
        if(num * 4 < ans)
            ans -= num;
        else
            ans += num;
    }

    return ans;
};
