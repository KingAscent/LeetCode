class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0

        for item in items:
            if ((ruleKey == "type" and ruleValue == item[0])
            or (ruleKey == "color" and ruleValue == item[1])
            or (ruleKey == "name" and ruleValue == item[2])):
                count += 1

        return count
