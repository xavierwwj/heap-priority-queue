"""
Context:
-To build a system that allows hospital patients with their uniquely assigned
health and illness
-Each time 2 patients are taken out of the system to be treated, 1 unit of time
will pass and the health will be updated.
-Any additions to patients should be sorted into the queue immediately, with
time taken to be t = 0.

Objective:
-To build a priority queue ADT using a heap data structure. A heap DS is chosen
because of its most ideal worse-case complexities of the operations required in
the context given.
-Allow inputs to be added into priority queue
-Allow retrieval of top priority items

"""
from math import floor

l = [5, 2, 95, 3, 6, 23, 45, 200, 4, 1]

## build_heap, min_heapify, insert, extract_min

def min_heapify(A, i):
    """
    Assumes that A[i] is the node that violates the min heap property, and that
    both its children are min-heaps. Swap A[i] with the min[2children]. Perform
    min_heapify() on the new index iteratively until no violation exists, or
    until no children exists for that index. 
    """
    while True:
        left = 2*i+1
        right = 2*i+2
        if right < len(A):
            # meaning both childs exist
            if A[i] > A[left]:
                if A[i] > A[right]:
                    if A[right] < A[left]:
                        # smallest = right
                        A[i], A[right] = A[right], A[i]
                        i = right
                    else:
                        # smallest = left
                        A[i], A[left] = A[left], A[i]
                        i = left
                else:
                    # smallest = left
                    A[i], A[left] = A[left], A[i]
                    i = left
            else:
                if A[i] > A[right]:
                    # smallest = right
                    A[i], A[right] = A[right], A[i]
                    i = right
                else:
                    break
        elif left < len(A):
            # meaning only left child exists and left child is a leaf
            if A[i] > A[left]:
                A[i], A[left] = A[left], A[i]
            break
        else:
            # meaning no child and this is a leaf
            break
    """
    A more concise but slightly less efficient solution
    
    if left < len(A) and A[left] < A[i]:
        smallest = left
    else:
        smallest = i
    if right < len(A) and A[right] < A[smallest]:
        smallest = right
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)
    """

def build_heap(A):
    # given last index n, i.e. n+1 items, floor((n-1)/2) gives the first index
    # to loop down to 0th index. Hence total items = 1 + floor((n-1)/2) =
    # floor(len(A)/2)
    for i in reversed(range(floor(len(A)/2))):
        min_heapify(A, i)

build_heap(l)

def insert(A, val):
    A.append(val)
    i = len(A)-1
    parent = floor((i-1)/2)
    while parent >= 0 and A[i] < A[parent]:
        A[i], A[parent] = A[parent], A[i]
        i = parent
        parent = floor((i-1)/2)

def extract_min(A):
    n = len(A) - 1
    A[0], A[n] = A[n], A[0]
    val = A.pop()
    min_heapify(A,0)
    return val
