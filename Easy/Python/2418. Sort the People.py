class Solution(object):
    def sortPeople(self, names, heights):
        ordered = {heights[i]:names[i] for i in range(len(names))}
        heights.sort(reverse = True)
        for i in range(len(heights)):
            names[i] = ordered[heights[i]]
        return names
