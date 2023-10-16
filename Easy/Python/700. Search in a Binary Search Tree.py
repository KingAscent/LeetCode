class Solution(object):
    def searchBST(self, root, val):
        while root and root.val != val:
            root = root.right if root.val < val else root.left
        
        return root
