from collections import deque

from binarytree import tree

import null as null


def max_dept(root: tree) -> int:
    if not root:
        return 0
    level = 0
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1

        return level


def max_dept_recursion(root) -> int:
    if not root:
        return 0
    return max(max_dept_recursion(root.left), max_dept_recursion(root.right)) + 1


i_root = [3, 9, 20, null, null, 15, 7]

print(max_dept_recursion(i_root))


'''
install binary tree
pip install binarytree
'''