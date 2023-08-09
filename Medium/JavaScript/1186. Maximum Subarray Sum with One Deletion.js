var maximumSum = function(arr) {
    let n = arr.length;
    let front = Array(n).fill(0);
    let back = Array(n).fill(0);
    let max = arr[0];

    // Going forward
    front[0] = arr[0];
    for(let i = 1; i < n; i++){
        front[i] = Math.max(arr[i], front[i - 1] + arr[i]);
        max = Math.max(max, front[i]);
    }

    // Going back
    back[n - 1] = arr[n - 1];
    for(let i = n - 2; 0 <= i; i--){
        back[i] = Math.max(arr[i], back[i + 1] + arr[i]);
    }

    // Find max sum
    for(let i = 1; i < n - 1; i++){
        max = Math.max(max, front[i - 1] + back[i + 1]);
    }

    return max;
};
