class Solution(object):
    def minOperations(self, boxes):
        # Initialize a list to contain the number of
        # operations
        ops = [0] * len(boxes)

        # Use a for loop to move all the balls to the ith box
        for i in range(len(boxes)):
            cost = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    cost += abs(i - j)
            ops[i] = cost

        # Return the ops list
        return ops
