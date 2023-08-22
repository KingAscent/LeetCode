class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] df = new int[n];
        
        if(0 < k){
            for(int i = 0; i < n; i++){
                int temp = 0;
                for(int j = 1; j <= k; j++){
                    temp += code[(i + j) % n];
                }
                df[i] = temp;
            }
        }else if(k < 0){
            for(int i = 0; i < n; i++){
                int temp = 0;
                for(int j = 1; j <= k * -1; j++){
                    temp += code[(i - j + n) % n];
                }
                df[i] = temp;
            }
        }

        return df;
    }
}
