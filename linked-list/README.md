# Linked List
This is experimental implementation of Singly Linked List

## What is Linked List? 
Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers. They include a series of connected nodes. Here, each node stores the data and the address of the next node.


## How it works?
``` python
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
>>> l.apend(7)
>>> l.apend(6)
>>> l.apend(3)
>>> m = l.sorted()
>>> m
[2, 3, 4, 6, 7]

```
