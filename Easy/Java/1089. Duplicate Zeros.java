class Solution {
    public void duplicateZeros(int[] arr) {
        int n = arr.length;
        for(int i = 0; i < n; i++){
            if(arr[i] == 0 && i + 1 < n){
                for(int j = n - 1; i + 1 < j; j--)
                    arr[j] = arr[j - 1];
                arr[i + 1] = 0;
                i++;
            }
        }
    }
}
