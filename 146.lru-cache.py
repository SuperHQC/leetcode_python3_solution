#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
# class Node:
#     def __init__(self, key, value) -> None:
#         self.key = key
#         self.val = value
#         self.prev = None
#         self.next = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.head = Node(-1, -1)
#         self.tail = self.head
#         self.storage = {}

#     def get(self, key: int) -> int:
#         if key in self.storage:
#             node = self.storage[key]
#             if node == self.tail:
#                 return node.val
#             node.prev.next = node.next
#             node.next.prev = node.prev
#             node.prev = self.tail
#             node.next = None
#             self.tail.next = node
#             self.tail = node
#             return node.val
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if self.get(key) != -1:
#             node = self.storage[key]
#             node.val = value
#         else:
#             node = Node(key, value)
#             self.storage[key] = node
#             self.tail.next = node
#             node.prev = self.tail
#             self.tail = node
#             if self.capacity < len(self.storage):
#                 victim = self.head.next
#                 del self.storage[victim.key]
#                 self.head.next = victim.next
#                 victim.next.prev = self.head



from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.storage = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.storage:
            res = self.storage[key]
            self.storage.move_to_end(key, True)
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        self.get(key)
        self.storage[key] = value
        if len(self.storage) > self.capacity:
            self.storage.popitem(False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

