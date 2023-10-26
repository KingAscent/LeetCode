class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root or (not root.left and not root.right):
            return 0
        
        this_sum = 0
        if root.left and not root.left.left and not root.left.right:
            this_sum += root.left.val
        
        return this_sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
