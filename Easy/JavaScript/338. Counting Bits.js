var countBits = function(n) {
    let ans = Array(n + 1);
    ans[0] = 0;

    for(let i = 1; i <= n; i++){
        if(i % 2 == 0)
            ans[i] = ans[i / 2];
        else
            ans[i] = ans[i - 1] + 1;
    }

    return ans;
};
