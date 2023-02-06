class Solution {
    public int shortestSequence(int[] rolls, int k) {
        // Initialize a variable and a set to keep track of the length
        // of the shortest sequence
        int seq = 1;
        Set<Integer> set = new HashSet<>();

        // Find each complete sequence
        for(int i : rolls){
            set.add(i);
            if(set.size() == k){
                seq++;
                set.clear();
            }
        }

        // Return length of the shortest sequence
        return seq;
    }
}
