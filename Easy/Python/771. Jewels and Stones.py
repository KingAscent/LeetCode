class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # Create a dictionary to contain the different types of jewels
        # Count of jewels amongst the stones
        types = {}
        count = 0
        
        # Add the different jewels into the dictionary
        for i in range(len(jewels)):
            types[i] = jewels[i]
        
        # Go over the stones, looking for jewels
        for i in range(len(stones)):
            if stones[i] in types.values():
                count += 1
        
        # Return the count of jewels
        return count
