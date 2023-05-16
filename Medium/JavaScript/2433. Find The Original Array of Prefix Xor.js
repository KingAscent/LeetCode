var findArray = function(pref) {
    let arr = Array(pref.length);
    arr[0] = pref[0];

    for(let i = pref.length - 1; 0 < i; i--){
        arr[i] = pref[i] ^ pref[i - 1];
    }

    return arr;
};
