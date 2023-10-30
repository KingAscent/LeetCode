class Solution(object):
    def distMoney(self, money, children):
        if money < children:
            return -1
        money -= children

        count = 0
        while 7 <= money and count != children:
            money -= 7
            count += 1
        
        if money != 0 and ((count == children) or (money == 3 and children - count == 1)):
            count -= 1
        
        return count
