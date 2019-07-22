a=[]

def inorder(bst,currNode):   #sorted (left first) 
	if(bst.root!=None):
	    if currNode!=None:
	    	inorder(bst,currNode.left)
	    	print(currNode.key)
	    	a.append
	    	inorder(bst,currNode.right)

def preorder(bst,currNode):		#root first
	if(bst.root!=None):
	    if currNode!=None:
	    	print(currNode.key)
	    	preorder(bst,currNode.left)
	    	preorder(bst,currNode.right)

def postorder(bst,currNode):
	if(bst.root!=None):
	    if currNode!=None:
	    	postorder(bst,currNode.left)
	    	postorder(bst,currNode.right)
	    	print(currNode.key)
