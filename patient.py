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
from modified_heap import build_heap, insert, extract_min

class patient_queue():
    def __init__(self):
        self.queue = []
        self.time = 0
        self.to_update = False

    def load_list(self, loc):
        """
        Runs at O(n) time
        """
        f = open(loc, "r")
        for line in f:
            temp = []
            digit = ''
            for char in line:
                if char == '\n':
                    if digit != '':
                        temp.append(int(digit))
                        digit = ''
                    break
                elif char == ' ':
                    temp.append(int(digit))
                    digit = ''
                else:
                    digit = digit + char
            self.queue.append(temp)
        build_heap(self.queue)
    
    def pop_patient(self):
        """
        Runs at O(log(n)) time when queue is not modified
        Runs at O(n) time when queue is modified

        Compare this with an unsorted array, which takes O(n) time
        for any case. Or with a sorted array which takes O(nlog(n)) to
        build in the first place, followed by O(1), O(nlog(n)) respectively
        """
        assert len(self.queue) != 0
        # standard list being the unmodified one
        # calculated list being a simple list with the updated health,
        # used for heapifying. Time passed = 1 unit
        patient = extract_min(self.queue)
        if self.to_update:
            for i in range(len(self.queue)):
                self.queue[i][0] -= self.queue[i][1]
            build_heap(self.queue)
        self.to_update = not self.to_update
        return patient

    def insert_patient(self, data):
        """
        Runs at O(log(n)) time. Sorted array takes O(nlog(n)) to insert.
        Unsorted array takes O(1).
        """
        insert(self.queue, data)

inst = patient_queue()
inst.load_list("patient_list.txt")


