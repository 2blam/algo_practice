# binary tree:
#				A
#			B		C

# 
# in-order: 	B, A, C / LEFT, ROOT, RIGHT
# pre-order: 	A, B, C / ROOT, LEFT, RIGHT
# post-order: 	B, C, A / LEFT, RIGHT, ROOT

class Node:
	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data


def inorder(root):
	if(root != None):
		inorder(root.left) 	# recur on left child
		print(root.data, end=" ") 	# print the data
		inorder(root.right) # recur on right child

def preorder(root):
	if(root != None):
		print(root.data, end=" ")	# print the data
		preorder(root.left) 	# recur on left child
		preorder(root.right)	# recur on right child

def postorder(root):
	if(root != None):
		postorder(root.left) 	# recur on left child
		postorder(root.right)	# recur on right child
		print(root.data, end=" ")	# print the data

# binary tree:
#				1
#			2		3
#		4		5

root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)

print("Tree:")
print("			1")
print("		2 		3")
print("	4 		5")

print("inorder B, A, C / LEFT, ROOT, RIGHT:")
inorder(root)
print()
print("*" * 10)

print("preorder A, B, C / ROOT, LEFT, RIGHT:")
preorder(root)
print()
print("*" * 10)

print("postorder B, C, A / LEFT, RIGHT, ROOT:")
postorder(root)
print()
print("*" * 10)