
from typing import List


def merge_sorted_matrix(A: List[list]):
    # In this case, complexity is O(2n^2), where for the purposes of
    # algorithm scalability we can just consider its complexity
    # exponential O(n^2).
    merged_matrix = []
    n = len(A[0])
    for a in range(n):
        merged_matrix += A[a]
    for i in range(len(merged_matrix)):
        for j in range(i + 1, len(merged_matrix)):
            if merged_matrix[i] > merged_matrix[j]:
                # Sort elements out of order
                merged_matrix[i] = merged_matrix[j]
                merged_matrix[j] = merged_matrix[i]
    return merged_matrix


def test_merge_sorted_matrix():
    A = [
        [1, 3, 5],
        [1, 2, 6],
        [4, 7, 8],
    ]
    assert merge_sorted_matrix(A) == [1, 1, 2, 3, 4, 5, 6, 7, 8]


test_merge_sorted_matrix()


class Node:
    right_node: 'Node' = None
    left_node: 'Node' = None
    content: int = None

    def __init__(self, content, left_node=None, right_node=None):
        self.content = content
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return f'Node (value: {self.content})'


class BinarySearchTree:
    root_node: Node

    def __init__(self, root_node=None):
        self.root_node = root_node


def get_closest_node_content(N: Node, x, closest_node_content):
    if abs(N.content - x) < abs(closest_node_content - x):
        closest_node_content = N.content
    if N.left_node:
        closest_node_content = get_closest_node_content(N.left_node, x, closest_node_content)
    if N.right_node:
        closest_node_content = get_closest_node_content(N.right_node, x, closest_node_content)
    return closest_node_content


def search_tree_for_closest_node_content(T: BinarySearchTree, x):
    # Initiate the closest difference with the value from the root node
    if T.root_node is not None:
        return get_closest_node_content(T.root_node, x, T.root_node.content)


def test_search_tree_for_closest_node_content():
    left_node_0_0 = Node(content=1)
    right_node_0_1 = Node(content=34)
    left_node_1_0 = Node(content=12)
    right_node_1_1 = Node(content=23)
    left_node_0 = Node(content=7, left_node=left_node_0_0, right_node=right_node_0_1)
    right_node_0 = Node(content=18, left_node=left_node_1_0, right_node=right_node_1_1)
    root_node = Node(content=10, left_node=left_node_0, right_node=right_node_0)
    T = BinarySearchTree(root_node=root_node)

    assert search_tree_for_closest_node_content(T, 8) == 7
    assert search_tree_for_closest_node_content(T, 22) == 23
    assert search_tree_for_closest_node_content(T, 100) == 34
    assert search_tree_for_closest_node_content(T, 0) == 1

    empty_tree = BinarySearchTree()
    assert search_tree_for_closest_node_content(empty_tree, 12) == None
    assert search_tree_for_closest_node_content(empty_tree, 0) == None


test_search_tree_for_closest_node_content()



def search_value(T: Node):
    sum = 0
    if T.value is not None:
        if T.value % 2 == 0:
            sum += T.value
        sum += search_value(T.right_node)
        sum += search_value(T.left_node)
    return sum


class Node:
    right_node: Node = None
    left_node: Node = None
    value: int = None
