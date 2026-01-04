import unittest
from BinaryTreeInorderTraversal import TreeNode, Solution


class TestBinaryTreeInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1: root = [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)  # <--
        root.right.right = TreeNode(7)  # <--
        expected = [4, 2, 5, 1, 6, 3, 7]
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    def test_empty_tree(self):
        # root = []
        root = None
        expected = []
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    def test_single_node(self):
        # root = [1]
        root = TreeNode(1)
        expected = [1]
        self.assertEqual(self.solution.inorderTraversal(root), expected)


if __name__ == "__main__":
    unittest.main()
