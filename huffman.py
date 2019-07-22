import queue

class HuffmanNode(object):
	def __init__(self,left=None,right=None,root=None):
		self.left = left
		self.right = right
		self.root = root
	def children(self):
		return((self.left,self.right))

freq = [(100,'f'),(9,'e'),(12,'d'),(13,'c'),(16,'b'),(45,'a')]

def create_tree(frequencies):
	p = queue.PriorityQueue()
	for value in frequencies:
		p.put(value)
	while p.qsize()>1:
		l,r = p.get(),p.get()
		node = HuffmanNode(l,r)
		p.put((l[0]+r[0],node))
	return p.get()

node = create_tree(freq)
print(node)

def walk_tree(node,prefix="",code={}):
	if isinstance(node[1].left[1],HuffmanNode):
		walk_tree(node[1].left,prefix+"0",code)
	else:
		code[node[1].left[1]] = prefix+"0"

	if isinstance(node[1].right[1],HuffmanNode):
		walk_tree(node[1].right,prefix+"1",code)
	else:
		code[node[1].right[1]] = prefix+"1"

	return(code)

code=walk_tree(node)
for i in sorted(freq,reverse=False):
	print(i[1], '{:6.2f}'.format(i[0]) , code[i[1]])