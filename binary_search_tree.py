# A specific type of tree data structure where every node(vertices)
# can have at most two children.
# left child is smaller than parent node,
# right child is greater than parent node.
# there is exclusive access to root node.
# this makes BST a sorted data structure
# every decision gets rid of half of the data
# this enables searching to be O(LogN) run time complexity
# the height of BST is the number of layers the tree has
# Layer one has 2^0 (i.e. 1) node, layer two has 2^1 i.e. 2 nodes,
# layer n has 2^(h-1) nodes ... where h is height of tree
# to have a balanced BST, the height must be kept at minimum (having approximately same no of nodes on both sides),
# e.g. having 5 nodes in left sides and zero node on right OR having 20 nodes on right and 2 on the left leads
# to an imbalanced BST. hence, the running time complexity can grow to O(N) instead of O(LogN)
# NB: A balanced BST have approximately same number of nodes in both sides of root node
# All operations on BST is predictable, O(LogN) running time complexity on average, and O(N) in worst case scenario
# Unlike Arrays and LinkedList that diff running complexity depending on the side you manipulate
