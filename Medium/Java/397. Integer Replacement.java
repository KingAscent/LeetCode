class Solution {
    public int integerReplacement(int n) {
        int count = checkCount(n);

        return count;
    }

    public int checkCount(int n){
        if(n == Integer.MAX_VALUE)
            return 32;
        if(n == 1)
            return 0;
        else if(n % 2 == 0)
            return 1 + checkCount(n / 2);
        else
            return 1 + Math.min(checkCount(n + 1), checkCount(n - 1));
    }
}
