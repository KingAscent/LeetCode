class Solution(object):
    def wateringPlants(self, plants, capacity):
        # Initialize a steps counter, and remember initial capacity
        steps = 1 # Enter the loop taking the first step
        initialCapacity = capacity

        # Go over the list watering all the plants
        for i in range(len(plants) - 1):
            capacity -= plants[i]
            # Check if we can water the next plant
            if(capacity < plants[i + 1]):
                steps += (2 * (i + 1))
                capacity = initialCapacity
            steps += 1

        # Return the number of steps
        return steps
