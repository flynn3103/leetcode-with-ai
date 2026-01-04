"""
You have a tree (connected nodes) where each node has some stones. 
You want to make the tree "balanced" by adding stones (you can only add, not remove).
For example:
        Node 1: 1 stone
            |
        Node 2: 4 stones
        /         \
  Node 3: 2     Node 4: 6
      |
  Node 5: 5

Check each connection (edge):

Node 1 ↔ Node 2: |1 - 4| = 3 ❌ (difference is 3, needs to be ≤ 1)
Node 2 ↔ Node 3: |4 - 2| = 2 ❌ (difference is 2, needs to be ≤ 1)
Node 2 ↔ Node 4: |4 - 6| = 2 ❌ (difference is 2, needs to be ≤ 1)
Node 3 ↔ Node 5: |2 - 5| = 3 ❌ (difference is 3, needs to be ≤ 1)

Solution: Add stones to make it balanced
The optimal way:

Add 2 stones to Node 3 → now has 4 stones
Add 1 stone to Node 2 → now has 5 stones
Add 3 stones to Node 1 → now has 4 stones

After adding stones:
Node 1: 4 stones (was 1)
            |
        Node 2: 5 stones (was 4)
        /         \
  Node 3: 4     Node 4: 6
      |
  Node 5: 5

"""

import heapq


def findMinStones(tree_nodes, tree_from, tree_to, stones):

    graph = [[] for _ in range(tree_nodes + 1)]
    for u, v in zip(tree_from, tree_to):
        graph[u].append(v)
        graph[v].append(u)

    max_heap = [(-stones[i], i + 1) for i in range(tree_nodes)]
    heapq.heapify(max_heap)

    visited = set()
    total_moves = 0

    while len(visited) < tree_nodes:
        neg_stone_count, current_node = heapq.heappop(max_heap)

        if current_node in visited:
            continue

        accumulated_stones = -neg_stone_count
        original_stones = stones[current_node - 1]
        total_moves += accumulated_stones - original_stones

        visited.add(current_node)

        for neighbor in graph[current_node]:
            new_stone_count = neg_stone_count + 1
            heapq.heappush(max_heap, (new_stone_count, neighbor))

    return total_moves
