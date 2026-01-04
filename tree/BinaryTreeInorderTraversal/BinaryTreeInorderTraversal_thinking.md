# Thinking: Binary Tree Inorder Traversal

## Problem Translation
The goal is to visit all nodes of a binary tree in "in-order": **Left Subtree -> Root -> Right Subtree**. We need to return the values in a list.

### Constraints & Edge Cases
-   `root` could be `None` (empty tree).
-   Tree could be skewed (all left or all right), meaning height could be $N$.
-   Value range is standard for LeetCode (not relevant for the logic).

---
### Thinking Journal
- **Initial Idea**: Corrected identified the inorder sequence as "Left-Root-Right" (e.g., 1-2-3) and proposed using recursion.
- **Initial Logic**: Thought about returning `None` for the base case and was unsure about how to handle the "Root" step (initially thought about comparing values like a Binary Search Tree).
- **AI Hint**: The AI clarified that we follow the structure (pointers) rather than comparing values. It also suggested returning an empty list `[]` for the base case instead of `None` to allow for clean list concatenation (`+`).
- **Refinement**: Moved toward the recursive pattern: `self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)`.

## Approach: Recursive (Implemented)
### Thinking
This is the most intuitive approach. Since a tree is a recursive data structure, we can define the traversal as:
1.  Recursively visit the left child.
2.  Append the current node's value.
3.  Recursively visit the right child.

### Why this works?
It follows the definition directly. The base case is when `root` is `None`, where we return an empty list.

### Complexity
-   **Time**: $O(N)$ where $N$ is the number of nodes, as we visit each node exactly once.
-   **Space**: $O(H)$ where $H$ is the height of the tree, due to the recursion stack. In the worst case (skewed tree), this is $O(N)$.
