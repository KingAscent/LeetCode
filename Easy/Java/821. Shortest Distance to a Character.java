class Solution {
    public int[] shortestToChar(String s, char c) {
        int len = s.length();
        int[] dist = new int[len];
        for(int i = 0; i < len; i++){
            dist[i] = len;
        }

        for(int i = 0; i < len; i++){
            if(s.charAt(i) == c){
                for(int j = 0; j < len; j++){
                    dist[j] = Math.min(dist[j], Math.abs(i - j));
                }
            }
        }

        return dist;
    }
}
