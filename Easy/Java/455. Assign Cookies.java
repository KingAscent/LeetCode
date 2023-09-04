class Solution {
    public int findContentChildren(int[] g, int[] s) {
        int count = 0;
        int i = 0;
        Arrays.sort(g);
        Arrays.sort(s);

        for(int j = 0; j < g.length; j++){
            while(i < s.length && s[i] < g[j])
                i++;
            if(i == s.length)
                break;
            i++;
            count++;
        }

        return count;
    }
}
