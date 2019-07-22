def Insert(bst,node):
	y=None
	x=bst.root
	while (x):
		y=x
		if(node.key<x.key):
			x=x.left
		else:			#node.key>x.key
			x= x.right
	node.parent = y

	if y == None:
		bst.root = node
	elif node.key<y.key:
		y.left = node
	else:
		y.right = node
		
	bst.size+=1

def InsertRecur(bst,Node):
	if(bst.root == None):
		bst.root = Node
	else:
		return mainInsertRecur(Node,bst.root)

def mainInsertRecur(Node,currNode):
	if(Node.key<currNode.key):
		if(currNode.left == None):
			currNode.left = Node
			Node.parent = currNode
		else:
			return mainInsertRecur(Node,currNode.left)
	elif(Node.key>currNode.key):
		if(currNode.right == None):
			currNode.right = Node
			Node.parent = currNode
		else:
			return mainInsertRecur(Node,currNode.right)
	else:
		print("Already in tree")
