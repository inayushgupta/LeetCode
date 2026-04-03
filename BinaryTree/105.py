# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Preorder = root --> left --> right
        # Inorder  = left --> root --> right
        # Preorder defines root and inorder gives inforation about left and right subtree

        # Algorithm -- Recursive
        # Check Preorder and get the root
        # Find the index of this root in inorder 
        # left of this root are left subtree of this root and similarly for right
        # recursively build the tree and return

        # global preorder index tracker
        pre_index = 0

        # coverting inorder array into hashmap for O(1) lookups for index
        # without this we have to go through the array every time creating 
        # worst case lookup as O(n)
        inorder_index = {x:y for y,x in enumerate(inorder)}

        # actual runner code
        # left  --> left boundary
        # right --> right boundary 
        def builder(left, right):

            nonlocal pre_index

            # base case
            if left > right:
                return None
        
            node_val = preorder[pre_index]
            new_node = TreeNode(node_val)
            
            # this is the actual position of the node we just created 
            # left of this position is the left subtree of this node
            # right of this position is the right subtree of this node.
            node_index = inorder_index[node_val]

            # next node
            pre_index += 1

            # building the rest of the tree
            new_node.left = builder(left, node_index - 1)
            new_node.right = builder(node_index + 1 ,right)

            return new_node

        return builder(0, len(inorder) - 1)

