# TODO: Add filter()

# vars dynamically typed
# None instead of null

# multiple declarations
import heapq
from collections import deque
import math
a, b = 1, 'abc'
x = y = z = 0   # separate reference assignments
y = 2
print(f'{x} {y} {z}')

# loops
# range takes third paramter for increment (set to -1 for reverse loop)
for i in range(5, 0, -1):
    print(i)
# 5 4 3 2 1

# math: division is decimal by default
print(5 / 2)  # 2.5
# int division rounds down
print(5 // 2)  # 2
print(3 // -2)  # -2
print(int(3 / -2))  # -1 as expected

print(10 % 3)
print(-10 % 3)  # weird compared to other c-based langs
print('fmod', math.fmod(-10, 3))
# math.floor()
# math.ceil()
# math.sqrt()
# math.pow(b, e)

# min/max
float("inf")
float("-inf")
# python numbers are actually infinite and never overflow

# lists
arr = [1, 2, 3]
# use as a stack:
arr.append(1)  # to back
arr.pop()  # from back, O(1)
arr.pop(0)  # from arbitrary index, O(n)
print(arr)

# using as a queue will result in O(n) popping using pop(0)
# better: collections.deque or queue.Queue, O(1) pop from left
queue = deque()
queue.append(0)  # right side
queue.append(1)
queue.append(2)
queue.pop()  # from right
print(queue)
queue.popleft()  # from left
print(queue)
queue.appendleft(4)

arr.insert(1, 7)  # idx, val
# O(n)

arr[0] = 0
# O(1)

n = 5
arr = [1] * n
# arr = range(0, 5) # NOT A LIST, an iterable range obj
print(len(arr))

print(arr[1:3])  # 1 through 3 inclusive exclusive
print(arr[1:])

# unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

# be careful, num on left must match num expecting on right

# using index
nums = [1, 2, 3]
for i in range(len(nums)):
    print(nums[i])

# using value
for n in nums:
    print(n)

# using both index and value (uses unpacking) idx, value
for i, n in enumerate(nums):
    print(i, n)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
# zip helper function: creates arr of pairs (merges two input lists)
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# reverse arr: in place
nums1.reverse()
print(nums1)
# alternative: nums1[::-1] shallow copy

# sorting
arr = [5, 4, 2, 3, 5]
arr.sort()  # in place
print(arr)
arr.sort(reverse=True)
print(arr)

# works on strings too
arr = ['apple', 'banana', 'c']
arr.sort()
print(arr)

# custom sort
arr.sort(key=lambda x: len(x))
print(arr)

# list comprehension
arr = [i for i in range(5)]
print(arr)
arr = [i+i for i in range(5)]
print(arr)

# 2D list
arr = [[0] * 4 for i in range(5)]
print(arr)
# problematic alternative: (due to pass by ref for objects)
arr = [[0] * 4] * 4
print(arr)
arr[0][0] = 1  # modifies all 4 rows
print(arr)

# strings very similar to lists but immutable
s = "abc"
print(s[0:2])

# creates a new string
s += "def"
print(s)
# thus any modification considered an O(n) operation

# int() and str() casts

# get ascii value of char
print(ord("a"))

strings = ["ab", "cd", "ef"]
print(" ".join(strings))

# hash sets (O(1) search, insert) unique elems
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))  # size

# determine if exists
print(1 in mySet)
mySet.remove(1)
print(1 in mySet)

# list to set
print(set([1, 2, 3]))
# set comprehension
mySet = {i for i in range(5)}

# hash maps
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))
print(myMap["alice"])
myMap.pop("alice")
print("alice" in myMap)

# dict comprehension: useful for making adjacency list
myMap = {i: 2*i for i in range(3)}
print(myMap)

# iterate through keys
for key in myMap:
    print(key, myMap[key])

# iterate through values
for val in myMap.values():
    print(val)

# iterate through both
for key, val in myMap.items():
    print(key, val)

# Tuples (arrays but mutable): often used as hashable keys (lists aren't hashable)
tup = (1, 2, 3)
print(tup[1])
# tup[0] = 10 # can't do this

# heaps: implemented with arrays under the hood (min heap)
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 2)
print(minHeap)
print(minHeap[0])

while len(minHeap):
    # pop highest priority elem and return its value
    print(heapq.heappop(minHeap))

# no max heap by default, workaround: multiply each value by -1 on push and pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -1)
heapq.heappush(maxHeap, -2)
while len(maxHeap):
    # pop highest priority elem and return its value
    print(-heapq.heappop(maxHeap))

# build heap from existing array (heapify)
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

# functions


def myFunc(n, m):
    return n * m

# nested functions: CAN modify values, but won't take effect outside, need to declare editable vars as nonlocal


def outer(a, b):
    c = "c"
    d = "d"

    def inner():  # has access to everything in outer
        c = "e"
        nonlocal d
        d = "e"
        return a + b + c + d

    result = inner()
    print(c)  # c (original)
    print(d)  # e (modified)
    return result


print(outer("a", "b"))

# classes


class MyClass:
    # ctor is dunder
    def __init__(self, nums):  # self is passed into every method of a class (like this)
        self.nums = nums  # creating a member var and assigning it
        self.size = len(nums)

    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()  # reference from other member function
