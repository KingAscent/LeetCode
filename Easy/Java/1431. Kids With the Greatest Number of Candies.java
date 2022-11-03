class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        // Create a list of boolean values that will be returned
        // Variable to keep track of the greatest amount of candy
        List<Boolean> greatest = new ArrayList<>();
        int max = 0;
        
        // Find the greatest amount of candy currently in the candies array
        for(int i = 0; i < candies.length; i++){
            max = Math.max(max, candies[i]);
        }
        
        // Go over the candies array, checking if adding extraCandies to the
        // element will make it larger than max
        for(int i = 0; i < candies.length; i++){
            if(max <= candies[i] + extraCandies)
                greatest.add(true);
            else
                greatest.add(false);
        }
        
        // Return the list of boolean values
        return greatest;
    }
}
