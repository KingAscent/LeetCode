class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int[] par = new int[seq.length()];
        int count = 0;

        for(int i = 0; i < seq.length(); i++){
            if(seq.charAt(i) == '('){
                count++;
                par[i] = count % 2;
            }else{
                par[i] = count % 2;
                count--;
            }
        }

        return par;
    }
}
