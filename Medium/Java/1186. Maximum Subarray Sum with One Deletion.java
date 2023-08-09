class Solution {
    public int maximumSum(int[] arr) {
        int n = arr.length;
        int[] front = new int[n];
        int[] back = new int[n];
        int max = arr[0];

        // Going forward
        front[0] = arr[0];
        for(int i = 1; i < n; i++){
            front[i] = Math.max(arr[i], front[i - 1] + arr[i]);
            max = Math.max(max, front[i]);
        }

        // Going back
        back[n - 1] = arr[n - 1];
        for(int i = n - 2; 0 <= i; i--){
            back[i] = Math.max(arr[i], back[i + 1] + arr[i]);
        }

        // Find max sum
        for(int i = 1; i < n - 1; i++){
            max = Math.max(max, front[i - 1] + back[i + 1]);
        }

        return max;
    }
}
