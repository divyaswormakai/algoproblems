from MinMax import FindMax, FindMin,MinRecur,MaxRecur
from search import Search,SearchRecur
from Insert import Insert,InsertRecur
from Delete import Del
from traversal import inorder,preorder,postorder
import unittest

class BinarySearchTree:
	def __init__(self,size):
		self.size = size
		self.root = None

	class Node:
		def __init__(self,key):
			self.key=key
			self.value=None
			self.left = None
			self.right =None
			self.parent = None

	def IncSize(self):
		self.size+=1

class Test(unittest.TestCase):
	def test_search(self):
		bst = BinarySearchTree(10)
		bst2 = BinarySearchTree(10)
		bst.IncSize()
		Root = bst.Node(50)
		n40 = bst.Node(40)
		n35 = bst.Node(35)
		n45 = bst.Node(45)
		n42 = bst.Node(42)
		n41 = bst.Node(41)
		n55 = bst.Node(55)
		n52 = bst.Node(52)

		RRoot = bst2.Node(50)
		Rn40 = bst2.Node(40)
		Rn35 = bst2.Node(35)
		Rn45 = bst2.Node(45)
		Rn42 = bst2.Node(42)
		Rn41 = bst2.Node(41)
		Rn55 = bst2.Node(55)

		InsertRecur(bst2,RRoot)
		InsertRecur(bst2,Rn40)
		InsertRecur(bst2,Rn35)
		InsertRecur(bst2,Rn45)
		InsertRecur(bst2,Rn42)
		InsertRecur(bst2,Rn41)

		Insert(bst,Root)
		Insert(bst,n40)
		Insert(bst,n35)
		Insert(bst,n55)
		Insert(bst,n42)
		Insert(bst,n41)
		Insert(bst,n52)

		self.assertEqual(Search(bst,n55),55)
		self.assertEqual(SearchRecur(bst2,Rn45),True)
		self.assertEqual(FindMin(bst),35)
		self.assertEqual(MinRecur(bst),35)
		self.assertEqual(FindMax(bst),55)
		self.assertEqual(MaxRecur(bst),55)
		self.assertEqual(Del(bst,n52),"Done")
		self.assertEqual(Search(bst,n52),False)



if __name__=="__main__":
	unittest.main()

	# print(Search(bst2,n55))

	# print(SearchRecur(bst,n55))
	# print(SearchRecur(bst2,n55))

	# print(FindMax(bst))
	# print(MaxRecur(bst))

	# print(Search(bst,n55))
	# Del(bst,n55)
	# n55 = bst.Node(55)
	# print(Search(bst,n55))	

	# print(SearchRecur(Root,n55))

	# print(inorder(bst,bst.root))
	# preorder(bst,bst.root)
	# postorder(bst,bst.root)
	
