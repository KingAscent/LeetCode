class Solution(object):
    def mySqrt(self, x):
        root = x
        
        while(x < root * root):
            root = (root + x / root) / 2
        
        return root
