class Solution(object):
    def shortestSequence(self, rolls, k):
        # Initialize a variable and a set to keep track of the length
        # of the shortest sequence
        seq = 1
        sequences = set()

        # Find each complete sequence
        for i in rolls:
            sequences.add(i)
            if len(sequences) == k:
                seq += 1
                sequences.clear()
        
        # Return the length of the shortest sequence
        return seq
