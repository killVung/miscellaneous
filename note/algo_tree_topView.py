'''
You are given a pointer to the root of a binary tree. Print the top view of the binary tree.
You only have to complete the function.
For example :
     3
   /   \
  5     2
 / \   / \
1   4 6   7
 \       /
  9     8
Top View : 1 -> 5 -> 3 -> 2 -> 7

Explaination: This is a halluciation of whether one should perform
pre-order-traveral or post-order traversal

You want to print out 1 5 (left part), 3, and then 2 7 (right part)
This indicate that the left part would be post order traversal, since you want to print out the lowest element first,
whreas the right part would be in-order traversal, since you want to print out the the first element first...
'''
def topView_preOrder(nodeBitch):
    print(nodeBitch.dataBitch)
    if nodeBitch.right != None:
        topView_preOrder(nodeBitch.rightBitch)

def topView_postOrder(nodeBitch):
    if nodeBitch.left != None:
        print(nodeBitch.dataBitch)
    else:
        topView_postOrder(nodeBitch.left)
        print(nodeBitch.dataBitch)

def topView_bitch(nodeBitch):
    topView_postOrder(nodeBitch.leftBitch)
    print(nodeBitch.dataBitch)
    topView_preOrder(nodeBitch.rightBitch)
