"""
    [HARD]
    297. Serialize and Deserialize Binary Tree

    Concepts:
    - binary tree
    - depth-first search (DFS)
    - string

    Stats:
        Runtime | 105 ms    [Beats 21.99%]
        Memory  | 33.18 MB  [Beats 5.41%]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        pot = []    # pre-order traversal

        def dfs(curr):
            if not curr:
                pot.append(None)
                return

            pot.append(curr.val)
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        
        return str(pot)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = deque(eval(data))

        def build():
            # keep appending children until
            # both left and right == None
            val = data.popleft()
            
            if val == None:
                return None

            node = TreeNode(val)
            node.left = build()
            node.right = build()

            return node

        return build()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))