class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        for(int i = 0; i < arr.length - 2; i++){
            boolean odd1 = arr[i] % 2 == 1;
            boolean odd2 = arr[i + 1] % 2 == 1;
            boolean odd3 = arr[i + 2] % 2 == 1;
            if(odd1 && odd2 && odd3)
                return true;
        }

        return false;
    }
}
