class Solution {
    public int countTriplets(int[] arr) {
        int count = 0;

        for(int i = 0; i < arr.length; i++){
            int temp = arr[i];
            for(int j = i + 1; j < arr.length; j++){
                // xor of element
                temp ^= arr[j];
                if(temp == 0)
                    count += j - i;
            }
        }

        return count;
    }
}
