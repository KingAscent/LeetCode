var maxArea = function(height) {
    let water = 0;
    let left = 0;
    let right = height.length - 1;

    while(left < right){
        let min = Math.min(height[left], height[right]);
        water = Math.max(water, min * (right - left));
        if(height[left] < height[right])
            left++;
        else
            right--;
    }

    return water;
};
