class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        # Base case
        if original is None:
            return None
        
        # Current node is cloned
        if original is target:
            return cloned
        
        # See if either left tree or right tree has a target
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
