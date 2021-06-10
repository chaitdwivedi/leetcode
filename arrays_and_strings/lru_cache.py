'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''


'''
Using OrderedDict
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

'''
Using Dict and Doubly Linked List - to maintain order 
'''

class DoublyLinkedNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = DoublyLinkedNode()
        self.tail = DoublyLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        "Adding node to start - making it most recently used"
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _pop_lru(self):
        result = self.tail.prev
        self._remove_node(result)
        return result

    def _make_mru(self, node):
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if not node:
            return -1

        self._make_mru(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            new_node = DoublyLinkedList(key=key, value=value)
            self.cache[key] = new_node
            self._add_node(new_node)

            if len(self.cache) > self.capacity:
                lru = self._pop_lru()
                del self.cache[lru.key]
        else:
            node.value = value
            self._make_mru(node)
