class Solution {
    public boolean validMountainArray(int[] arr) {
        int n = arr.length;
        if(n < 3)
            return false;
        int l = 0;
        int r = n - 1;

        // Double pointers
        while(l < n - 2 && arr[l] < arr[l + 1]){
            l++;
        }
        while(1 < r && arr[r] < arr[r - 1]){
            r--;
        }

        return l == r;
    }
}
