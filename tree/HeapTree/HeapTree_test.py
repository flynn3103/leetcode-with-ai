from HeapTree import findMinStones


def test_example_from_docstring():
    # Tree:
    # 1-2, 2-3, 2-4, 3-5
    tree_nodes = 5
    tree_from = [1, 2, 2, 3]
    tree_to = [2, 3, 4, 5]
    stones = [1, 4, 2, 6, 5]
    # Expected minimal added stones = 6
    assert findMinStones(tree_nodes, tree_from, tree_to, stones) == 6


def test_already_balanced_chain():
    # 1-2-3-4, stones already satisfy |diff| ≤ 1
    tree_nodes = 4
    tree_from = [1, 2, 3]
    tree_to = [2, 3, 4]
    stones = [5, 4, 5, 4]
    assert findMinStones(tree_nodes, tree_from, tree_to, stones) == 0


def test_two_nodes_simple():
    # 1-2, stones [3,0] -> need to raise node 2 to 2 (total +2)
    tree_nodes = 2
    tree_from = [1]
    tree_to = [2]
    stones = [3, 0]
    assert findMinStones(tree_nodes, tree_from, tree_to, stones) == 2


def test_star_center_high():
    # Center 1 connected to 2,3,4; center=10, leaves=1
    # Each leaf must be at least 9 -> add 8 per leaf = 24 total
    tree_nodes = 4
    tree_from = [1, 1, 1]
    tree_to = [2, 3, 4]
    stones = [10, 1, 1, 1]
    assert findMinStones(tree_nodes, tree_from, tree_to, stones) == 24


def test_path_two_maxima():
    # Path 1-2-3-4-5, A=[10,0,0,0,10]
    # Envelope yields additions [0,9,8,9,0] => 26
    tree_nodes = 5
    tree_from = [1, 2, 3, 4]
    tree_to = [2, 3, 4, 5]
    stones = [10, 0, 0, 0, 10]
    assert findMinStones(tree_nodes, tree_from, tree_to, stones) == 26


def test_single_node():
    tree_nodes = 1
    tree_from = []
    tree_to = []
    stones = [7]
    assert findMinStones(tree_nodes, tree_from, tree_to, stones) == 0
