def Del(bst,node):
	x=bst.root
	while(x!=None):
		if(x.key == node.key):
			if(node.left==None and node.right ==None):
				# if node had no child then parent of node is changed
				if(node.key<node.parent.key):
					node.parent.left=None
				else:
					node.parent.right=None

			elif(node.left == None and node.right !=None):
				# if node has a right child then right child is replaced as node
				rightChild = node.right
				while(rightChild.left != None):
					rightChild = rightChild.left
				if(rightChild==node.right):
					node.right = None
				else:
					rightChild.left = None
				node.key = rightChild.key

			elif(node.left != None and node.right ==None):
				# if node has a left child then left child is replaced as node
				leftChild = node.left
				while(leftChild.left != None):
					leftChild = leftChild.left
				if(leftChild==node.left):
					node.left = None
				else:
					leftChild.left = None
				node.key = leftChild.key

			else:
				# if node has a left and right child then leftmost leaf of the right child is taken to reaplce
				rightNode=node.right

				while(rightNode):
					if(rightNode.left!=None):
						rightNode = rightNode.left
					else:
						break
				if(rightNode == node.right):
					node.key = rightNode.key
					node.right = rightNode.right
					print(node.right)
				else:
					node.key = rightNode.key
					rightNode.left = None

			node.parent = None
			return "Done"
			break
				
		elif(x.key< node.key):
			x=x.right

		else:            #x.key > node.key):
			x=x.left
