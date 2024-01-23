class TreeNode:

    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

    def bfs(self):

        queue = [self]

        ans = []

        while queue:
            current = queue.pop(0)
            ans.append(current.data)

            if(current.left):
                queue.append(current.left)

            if(current.right):
                queue.append(current.right)

        return ans
    
    def dfs(self,stack):

        if(self is None):
            return stack
        
        if(self.left):
            self.left.dfs(stack)

        stack.append(self.data)

        if(self.right):
            self.right.dfs(stack)

        return stack

# Define tree nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

# Build the tree structure
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# This creates the following tree:
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7

print(node1.bfs())
print(node1.dfs([]))