class Solution {
    public int countVowelStrings(int n) {
        int a = 1, e = 1, i = 1, o = 1, u = 1;

        for(int j = 1; j < n; j++){
            a = a + e + i + o + u;
            e = e + i + o + u;
            i = i + o + u;
            o = o + u;
            // u doesn't change
        }

        return a + e + i + o + u;
        
        /*
        One liner solution:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) / 24;
        */
    }
}
