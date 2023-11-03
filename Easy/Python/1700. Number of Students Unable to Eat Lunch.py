class Solution(object):
    def countStudents(self, students, sandwiches):
        zeros = 0
        ones = 0

        for n in students:
            if n == 0:
                zeros += 1
            else:
                ones += 1
        
        for n in sandwiches:
            if (n == 0 and zeros == 0) or (n == 1 and ones == 0):
                break
            if n == 0:
                zeros -= 1
            else:
                ones -= 1
        
        return max(zeros, ones)
