class Solution {
    public int pivotInteger(int n) {
        int pivot = -1;
        int left = 0;

        for(int i = 0; i <= n; i++){
            left += i;
            int right = 0;
            
            for(int j = i; j <= n; j++)
                right += j;
            
            if(left == right)
                pivot = i;
        }

        return pivot;
    }
}
