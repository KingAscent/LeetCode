class Solution(object):
    def checkSymmetry(self, leftTree, rightTree):
        if not leftTree and not rightTree:
            return True
        
        if leftTree and rightTree and leftTree.val == rightTree.val:
            outer = self.checkSymmetry(leftTree.left, rightTree.right)
            inner = self.checkSymmetry(leftTree.right, rightTree.left)
            return outer and inner
        
        return False
    
    def isSymmetric(self, root):
        return self.checkSymmetry(root, root)
