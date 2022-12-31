class Solution {
    public int[] sumZero(int n) {
        int[] myArray = new int[n];
        int sum = 0;

        for(int i = 1; i < n; i++){
            sum += i;
            myArray[i] = i;
        }
        
        myArray[0] -= sum;

        return myArray;
    }
}
