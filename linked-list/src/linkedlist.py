from inspect import stack, currentframe
from collections import Iterator

__all__ = [
    'LinkedList'
]


class LinkedList:
    """Singly linked-list

    see also https://gist.githubusercontent.com/katryo/2965919/raw/993ee3bd71b11a113356c9cf00407e381debc2be/linkedlist.py

    Example:
    >>> from linkedlist import LinkedList
    >>> l = LinkedList()

    # append a new item into Linked List at the last position
    >>> l.append(1)
    >>> l.append(2)
    >>> l.append(3)
    >>> l
    [1, 2, 3]

    # insert a new item into Linked List at the position which is retrieved from argument
    >>> l.insert(4, 1)
    >>> l
    [1, 4, 2, 3]

    # remove the last item
    >>> l.pop_back()
    >>> l
    [1, 4, 2]

    # remove the first item
    >>> l.pop_front()
    >>> l
    [4, 2]

    # sorting
    >>> l.append(7)
    >>> l.append(6)
    >>> l.append(3)
    >>> m = l.sorted()
    >>> m
    [2, 3, 4, 6, 7]

    """
    __slot__ = ['head', 'size', 'debug']

    def __init__(self, debug=False):
        self.head = _Node(None)
        self.size = 0
        self.debug = debug

    def __str__(self):
        ret = '['
        t = self.head.next
        while t:
            ret += str(t.value)
            t = t.next
            if t:
                ret += ", "

        ret += ']'
        return ret

    def __repr__(self):
        if self.debug:
            ret = ''
            t = self.head
            while t:
                ret += f"id:{id(t)}, next:{id(t.next)}, value:{t.value}\n"
                t = t.next

            return ret
        else:
            return self.__str__()

    def __iter__(self):
        return self._LinkedListIterator(self.head)

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        res = self.head.next
        for _ in range(idx):
            res = res.next
        return res.value

    def __setitem__(self, idx: int, value):
        res = self.head.next
        for _ in range(idx):
            res = res.next
        res.value = value

    def __add__(self, obj):
        res = LinkedList()

        for xi in self:
            res.append(xi)
        for yi in obj:
            res.append(yi)
        return res

    def __eq__(self, obj):
        x = self.head.next
        y = obj.head.next

        if self.size != obj.size:
            return False

        for i in range(self.size):
            if x.value != y.value:
                return False
            x = x.next
            y = y.next

        return True

    def __ne__(self, obj):
        return not self.__eq__(obj)

    def _get_item(self, pos):
        prev_node = self.head
        next_node = prev_node.next
        for _ in range(pos):
            prev_node = next_node
            next_node = next_node.next
        return prev_node, next_node

    def append(self, value):
        """ Append a new item to the end of the LinkedList.

        Has the following public attributes:

        * value : Any
            The new item to append

        Complexity is O(1)
        """
        self.insert(value, self.size)

    def insert(self, value, pos: int):
        """ Insert a new item into the LinkedList at position pos.

        Has the following public attributes:

        * value : Any
            The new item to append
        * pos : int
            The position of the LinkedList to append a new item

        Complexity is O(N)
        """

        if pos > self.size+1 or pos < 0:
            raise IndexError

        prev_node, next_node = self._get_item(pos)

        cur_node = _Node(value)
        prev_node.next = cur_node
        if pos < self.size+1:
            cur_node.next = next_node

        self.size += 1

    def pop_back(self):
        """ 
        Remove the item from the end of the LinkedList. 

        Complexity is O(N)
        """
        if self.size == 0:
            raise IndexError

        prev_node, last_node = self._get_item(self.size-1)

        del last_node
        prev_node.next = None
        self.size -= 1

    def pop_front(self):
        """ 
        Remove the item from the head of the LinkedList. 

        Complexity is O(1)
        """
        if self.size == 0:
            raise IndexError
        head_node = self.head
        target_node = head_node.next
        next_node = head_node.next.next

        del target_node
        head_node.next = next_node
        self.size -= 1

    def sorted(self):
        """ 
        Return sorted LinkedList. 

        Complexity is O(NlogN)
        """
        if self.size < 1:
            return self
        pivot = self.head.next
        next_node = pivot.next
        left = LinkedList()
        right = LinkedList()

        while next_node:
            if next_node.value <= pivot.value:
                left.append(next_node.value)
            else:
                right.append(next_node.value)
            next_node = next_node.next
        left = left.sorted()
        right = right.sorted()
        left.append(pivot.value)
        return left + right

    class _LinkedListIterator(Iterator):
        """An iterator of Singly Linked List.

        Has the following public attributes:

        * head : LinkedList
            The first node in LinkedList
        """
        __slot__ = ['head']

        def __init__(self, head):
            self.head = head.next

        def __next__(self):
            if self.head is None:
                raise StopIteration
            result = self.head
            self.head = self.head.next
            return result.value


class _Node:
    """An element in linked-list

    Has the following public attributes:

    * value : Any
        The item with valuee.
    """
    __slot__ = ['value', 'next']

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"id:{id(self)}, value:{self.value}, next:{id(self.next)}"

    def __repr__(self):
        if self.next:
            return f"id: {id(self)}, value: {self.value}, next: {id(self.next)}\n -> {self.next}"
        else:
            return f"id:{id(self)}, value:{self.value}, next:{self.next}"

    def __eq__(self, obj):
        return id(self) == id(obj)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
