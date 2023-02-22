class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int start = 0;
        int end = 0;

        for(int i : weights){
            start = Math.max(start, i);
            end += i;
        }

        while(start <= end){
            int mid = start + ((end - start) / 2);
            int cap = findDay(weights, mid);
            if(cap <= days)
                end = mid - 1;
            else
                start = mid + 1;
        }

        return start;
    }

    public int findDay(int[] weights, int mid){
        int date = 0;
        int sum = 0;

        for(int i = 0; i < weights.length; i++){
            if(sum + weights[i] <= mid){
                sum += weights[i];
            }else{
                sum = weights[i];
                date++;
            }
        }

        return date + 1;
    }
}
