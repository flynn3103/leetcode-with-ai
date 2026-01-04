# Link: https://neetcode.io/problems/binary-tree-inorder-traversal/question?list=allNC

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return (
            self.inorderTraversal(root.left)  # Step 1: Left
            + [root.val]  # Step 2: Root
            + self.inorderTraversal(root.right)  # Step 3: Right
        )
