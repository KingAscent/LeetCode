class Solution {
    public int[] minOperations(String boxes) {
        // Initialize an array to contain the number of
        // operations
        int[] ops = new int[boxes.length()];

        // Use a for loop to move all the balls to the ith box
        for(int i = 0; i < boxes.length(); i++){
            int cost = 0;
            for(int j = 0; j < boxes.length(); j++){
                if(boxes.charAt(j) == '1')
                    cost += Math.abs(i - j);
            }
            ops[i] = cost;
        }

        // Return the ops array
        return ops;
    }
}
