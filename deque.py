
class Node:
	"""
	A class for a node in a doubly-linked list, storing
	a data payload and links to next and previous nodes.
	"""

	def __init__(self, data = None, prev = None, next = None):
		"""Initialize the node with data payload and link to next node."""
		self.data = data
		self.next = next
		self.prev = prev

	def getdata(self):
		"""Get the node's data payload."""
		return self.data

	def setdata(self, data = None):
		"""Set the node's data payload."""
		self.data = data

	def getnext(self):
		"""Get the next linked node."""
		return self.next

	def setnext(self, node = None):
		"""Set the next linked node."""
		self.next = node

	def getprev(self):
		"""Get the previous linked node."""
		return self.prev

	def setprev(self, node = None):
		"""Set the previous linked node."""
		self.prev = node

class Deque:
	"""
	A double-ended queue supporting accessing
	the items at either end of the container.
	"""

	def __init__(self):
		"""Initializes an empty deque storing both head and tail nodes."""
		self.head = None
		self.tail = None

	def __iter__(self):
		"""Returns a forward iterator over the deque."""
		node = self.head
		while node is not None:
			yield node.getdata()
			node = node.getnext()

	def __reversed__(self):
		"""Returns a reverse iterator over the deque."""
		node = self.tail
		while node is not None:
			yield node.getdata()
			node = node.getprev()

	def __str__(self):
		"""Returns a string representation of the deque."""
		return " -> ".join([str(x) for x in self])

	def __repr__(self):
		"""Returns a printable representation of the deque."""
		return str(self)

	def __len__(self):
		"""Returns the length of the deque."""
		size = 0
		for i in self:
			size += 1
		return size

	### Problem 1
	def push(self, data):
		"""
		Adds a new item to the front of the deque.
		:param data: The new item to prepend to the deque.
		:returns: None
		"""

		if data is not None:
			# for empty deque
			if self.head is None:
				n = Node(data=data)
				self.head = n
				self.tail = n
			# for non-empty deque
			else:
				n = Node(data=data, prev=None, next=self.head)
				self.head.setprev(n)
				self.head = n
		else:
			return None


	### Problem 2
	def pop(self):
		"""
		Removes and returns the front item of the deque.
		:returns: The item removed from the front deque, or None if empty.
		"""

		if len(self) > 1:
			temp_head = self.head
			self.head = self.head.getnext()
			self.head.setprev(None)
			return temp_head.getdata()

		elif len(self) == 1:
			temp_head = self.head
			self.head = None
			self.tail = None
			return temp_head.getdata()

		else:
			return None


	def peek(self):
		"""
		Returns the front item of the deque (without removing it).
		:returns: The item at the front of the deque, or None if empty.
		"""
		if self.head is not None:
			return self.head.getdata()


	### Problem 3
	def push_back(self, data):
		"""
		Adds a new item to the back of the deque.
		:param data: The new item to append to the deque.
		:returns: None
		"""
		if data is not None:

			# for empty deque
			if self.head is None:
				n = Node(data=data)
				self.head = n
				self.tail = n
			# for non-empty deque
			else:
				n = Node(data=data, prev=self.tail, next=None)
				self.tail.setnext(n)
				self.tail = n
		else:
			return None


	### Problem 4
	def pop_back(self):
		"""
		Removes and returns the item at the back of the deque.
		:return: The item removed from the back of the deque, or None if empty.
		"""

		if len(self) > 1:
			temp_tail = self.tail
			self.tail = self.tail.getprev()
			self.tail.setnext(None)
			return temp_tail.getdata()

		elif len(self) == 1:
			temp_tail = self.tail
			self.head = None
			self.tail = None
			return temp_tail.getdata()

		else:
			return None


	def peek_back(self):
		"""
		Returns the item at the back of the deque (without removing it).
		:returns: The item at the back of the deque, or None if empty.
		"""
		if self.tail is not None:
			return self.tail.getdata()


	### Problem 5
	def find(self, value):
		"""
		Finds the index of the given value in the deque.
		:param value: The value to search for in the deque.
		:returns: The index of the value if it exists; otherwise, None.
		"""

		head_node = self.head
		index = 0
		while head_node is not None:
			if head_node.getdata() == value:
				return index
			else:
				head_node = head_node.getnext()
				index += 1
		return None


	def print_nodes(self):
		"""
		prints out node information to the terminal for each node in order
		from head to tail of the deque.
		:return: None
		"""
		head_node = self.head
		index = 0
		print("- index - prev - data - next -")
		for i in range(len(self)):
			if head_node.getprev() is not None:
				prev = head_node.getprev().getdata()
			else:
				prev = None
			if head_node.getnext() is not None:
				next = head_node.getnext().getdata()
			else:
				next = None
			node_data = head_node.getdata()

			print("- ", index,
				  " - ", prev,
				  " - ", node_data,
				  " - ", next,
				  " -", sep="")
			index += 1
			head_node = head_node.getnext()





