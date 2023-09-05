class Solution {
    public int findLucky(int[] arr) {
        Arrays.sort(arr);
        int[] count = new int[arr[arr.length - 1] + 1];
        int largest = -1;
        
        for(int n : arr)
            count[n]++;
        for(int i = 1; i < count.length; i++){
            if(count[i] == i)
                largest = i;
        }

        return largest;
    }
}
