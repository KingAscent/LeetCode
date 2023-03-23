class Solution {
    public int hIndex(int[] citations) {
        int len = citations.length;
        int[] arr = new int[len + 1];

        for(int num : citations){
            if(len <= num)
                arr[len]++;
            else
                arr[num]++;
        }

        int count = 0;
        for(int i = len; 0 <= i; i--){
            count += arr[i];
            if(i <= count)
                return i;
        }

        return 0;
    }
}
