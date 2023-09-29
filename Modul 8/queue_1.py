####    Nomor 4     ####
class Queue():
    def __init__(self):
        self.qlist = []
    def is_empty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist.pop(0)
    def get_front_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[0]
    def get_rear_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[-1]

Y = Queue()
Y.enqueue(43)
Y.enqueue(21)
Y.enqueue(7)
Y.enqueue(38)
Y.enqueue(16)

print(Y.get_front_most())
print(Y.get_rear_most())
print(Y.qlist)

####    Nomor 5     ####
class PriorityQueue():
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def get_front_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[0]
    def get_rear_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[-1]
    def dequeue(self):
        A = []
        for i in self.qlist:
            A.append(i)
        s = 0
        for i in range(1, len(self.qlist)):
            if A[i].priority < A[s].priority:
                s = i
        hasil = self.qlist.pop(s)
        return hasil.item

class _PriorityQEntry():
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

f = PriorityQueue()
f.enqueue("Predator",3)
f.enqueue("Omen",5)
f.enqueue("ROG",1)
f.enqueue("Legion",2)
f.enqueue("Victus",4)

print(f.dequeue())
print(f.dequeue())
print(f.dequeue())
print(f.dequeue())
print(f.dequeue())