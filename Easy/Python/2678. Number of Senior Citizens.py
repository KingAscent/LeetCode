class Solution(object):
    def countSeniors(self, details):
        count = 0

        for s in details:
            if int(s[11:13]) > 60:
                count += 1

        return count
