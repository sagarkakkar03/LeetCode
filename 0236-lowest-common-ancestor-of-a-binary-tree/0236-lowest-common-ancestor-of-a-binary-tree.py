# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def search(root):
            nonlocal ans
            left = right = False
            if root == p or root == q:
                if root.left:
                    left = search(root.left)
                if root.right:
                    right = search(root.right)
                if left or right:
                    ans = root
                return True
            if root.left:
                left = search(root.left)
            if root.right:
                right = search(root.right)
            if left == right == True:
                ans = root
            print(root.val, ans, left, right)
            if left or right:
                return True
            return False
        search(root)
        return ans