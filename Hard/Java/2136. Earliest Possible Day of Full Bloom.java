class Solution {
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        int max = 0;
        for(int i : growTime){
            max = Math.max(max, i);
        }

        int[] arr = new int[max + 1];
        int temp = 0;
        int min = 0;

        for(int i = 0; i < plantTime.length; i++){
            arr[growTime[i]] += plantTime[i];
        }

        for(int i = max; 0 < i; i--){
            if(arr[i] != 0){
                temp += arr[i];
                min = Math.max(min, temp + i);
            }
        }

        return min;
    }
}
