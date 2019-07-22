def Search(bst,node):
	x=bst.root
	while(x):
		if(x.key==node.key):
			return x.key
		elif(x.key >node.key):
			x=x.left
		elif(x.key < node.key):
			x=x.right
		
		if not x:
			return False

	return False

def SearchRecur(bst,searchNode):
	if(bst.root!=None):
		return MainSearchRecur(searchNode,bst.root)
	else:
		print(False)

def MainSearchRecur(searchNode,currNode):
	if(searchNode.key == currNode.key):
		return True
	elif(searchNode.key< currNode.key):
		if(currNode.left!=None):
			return MainSearchRecur(searchNode,currNode.left)
		else:
			return False
	elif(searchNode.key> currNode.key):
		if(currNode.right!=None):
			return MainSearchRecur(searchNode,currNode.right)
		else:
			return False
	else:
		return False
