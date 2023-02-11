class Solution {
    public int maxDepth(String s) {
        int depth = 0;
        int open = 0;

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                open++;
                depth = Math.max(depth, open);
            }
            if(s.charAt(i) == ')')
                open--;
        }

        return depth;
    }
}
