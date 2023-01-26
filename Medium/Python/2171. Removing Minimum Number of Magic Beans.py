class Solution(object):
    def minimumRemoval(self, beans):
        # Initialize values to store maximum and beanSum
        # Then sort the array
        maximum = 0
        beanSum = 0
        beans.sort()

        # Use a for loop to remove the beans from the bags with
        # the least amount of beans in them until each non-empty
        # bag has the same number of beans
        for i in range(len(beans)):
            beanSum += beans[i]
            maximum = max(maximum, beans[i] * (len(beans) - i))
        
        # Return the amount of beans that had to be removed
        return beanSum - maximum
