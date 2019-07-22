def FindMin(bst):
	x=bst.root
	while(x):
		if(x.left):
			x=x.left
		else:
			return x.key

def FindMax(bst):
	x=bst.root
	while(x):
		if(x.right):
			x=x.right
		else:
			return x.key

def MinRecur(bst):
	if(bst.root!=None):
		return MainMinRecur(bst.root)

def MainMinRecur(currNode):
	if(currNode.left!=None):
		return MainMinRecur(currNode.left)
	return currNode.key

def MaxRecur(bst):
	if(bst.root!=None):
		return MainMaxRecur(bst.root)

def MainMaxRecur(currNode):
	if(currNode.right!=None):
		return MainMaxRecur(currNode.right)
	return currNode.key