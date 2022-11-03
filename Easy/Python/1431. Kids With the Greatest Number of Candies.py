class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # Create a list of boolean values that will be returned
        # Variable to keep track of the greatest amount of candy
        greatest = []
        mostCandies = 0
        
        # Find the greatest amoutn of candy currently in the candies array
        for i in range(len(candies)):
            mostCandies = max(mostCandies, candies[i])
        
        # Go over the candies list, checking if adding extra crandies to the
        # element will make it larger than mostCandies
        for i in range(len(candies)):
            if mostCandies <= (candies[i] + extraCandies):
                greatest.append(True)
            else:
                greatest.append(False)
        
        # Return the list of boolean values
        return greatest
