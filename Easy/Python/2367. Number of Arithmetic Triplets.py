class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        count = 0
        mySet = set()
        
        for n in nums:
            if (n - diff) in mySet and (n - diff * 2) in mySet:
                count += 1
            mySet.add(n)

        return count
