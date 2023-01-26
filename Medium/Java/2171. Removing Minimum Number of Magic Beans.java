class Solution {
    public long minimumRemoval(int[] beans) {
        // Initialize long values to store max and sum
        // Then sort the array
        long max = 0;
        long sum = 0;
        Arrays.sort(beans);
        
        // Use a for loop to remove the beans from the bags with
        // the least amount of beans in them until each non-empty
        // bag has the same number of beans
        for(int i = 0; i < beans.length; i++){
            sum += beans[i];
            max = Math.max(max, (long) beans[i] * (beans.length - i));
        }

        // Return the amount of beans that had to be removed
        return sum - max;
    }
}
