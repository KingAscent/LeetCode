class Solution {
    public int countDistinctIntegers(int[] nums) {
        // Initialize a set to keep track of each individual num
        // Sets do not allow duplicate elements so similar numbers are ignored
        Set<Integer> numbers = new HashSet();

        // For each number in nums, first add the number
        // Then reverse the number and add it to the set
        for(int n : nums){
            numbers.add(n);
            int numR = 0; // Variable for the number reversed
            while(n != 0){
                // Evaluate each number in reverse order
                numR = numR * 10 + (n % 10);
                n /= 10;
            }
            numbers.add(numR);
        }

        // Return the size of the set
        return numbers.size();
    }
}
