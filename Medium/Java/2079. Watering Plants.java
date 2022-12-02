class Solution {
    public int wateringPlants(int[] plants, int capacity) {
        // Initialize a steps counter, and remember initial capacity
        int steps = 1; // Enter the loop taking the first step
        int initialCapacity = capacity;

        // Go over the array watering all the plants
        for(int i = 0; i < plants.length - 1; i++){
            capacity -= plants[i];
            // Check if we can water the next plant
            if(capacity < plants[i + 1]){
                steps += 2 * (i + 1);
                capacity = initialCapacity;
            }
            steps++;
        }

        // Return the number of steps
        return steps;
    }
}
