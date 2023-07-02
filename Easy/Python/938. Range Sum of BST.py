class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root == None:
            return 0
        
        this_sum = 0
        if low <= root.val <= high:
            this_sum = root.val
        if low < root.val:
            this_sum += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            this_sum += self.rangeSumBST(root.right, low, high)

        return this_sum
