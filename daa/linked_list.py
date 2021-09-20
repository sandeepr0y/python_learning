class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyLinkedList(object):

    def __init__(self, data_iter=None):
        self.first = None
        if data_iter:
            for d in reversed(data_iter):
                self.prepend(d)

    def prepend(self, data):
        n = Node(data)
        if self.first is not None:
            n.next = self.first
        self.first = n

    def append(self, data):
        n = Node(data)
        if self.first is None:
            self.first = n
        else:
            _pre_n = None
            for _n in self:
                _pre_n = _n
            _pre_n.next = n

    def insert(self, idx, data):
        n = Node(data)
        if idx == 0:
            self.prepend(n)
        else:
            for _idx, _n in enumerate(self, 0):
                if _idx == (idx - 1):
                    n.next = _n.next
                    _n.next = n
                    break
            else:
                raise IndexError('linked list index out of range')

    def pop(self):
        d = self.first.data
        self.first = self.first.next
        return d

    def remove(self, idx):
        if idx == 0:
            self.pop()
        else:
            for _idx, _n in enumerate(self, 0):
                if _idx == (idx - 1):
                    _n.next = _n.next.next
                    break
            else:
                raise IndexError('linked list index out of range')

    def __iter__(self):
        n = self.first
        while n:
            yield n
            n = n.next

    def __len__(self):
        counter = 0
        for n in self:
            counter += 1
        return counter

    def __repr__(self):
        s = ''
        for n in self:
            s += '[%s]-->' % n.data
        return s.rstrip('-->')


if __name__ == '__main__':
    ll = MyLinkedList(('A', 'B', 'C',))
    print(ll)
    # [A]-->[B]-->[C]

    ll.prepend('I')
    ll.prepend('J')
    ll.prepend('K')
    print(ll)
    # [K]-->[J]-->[I]-->[A]-->[B]-->[C]

    ll.append('X')
    ll.append('Y')
    ll.append('Z')
    print(ll)
    # [K]-->[J]-->[I]-->[A]-->[B]-->[C]-->[X]-->[Y]-->[Z]

    ll.insert(1, 'G')
    print(ll)
    # [K]-->[G]-->[J]-->[I]-->[A]-->[B]-->[C]-->[X]-->[Y]-->[Z]

    print('Pop: %s' % ll.pop())
    # Pop: K
    print(ll)
    # [G]-->[J]-->[I]-->[A]-->[B]-->[C]-->[X]-->[Y]-->[Z]

    ll.remove(3)
    print(ll)
    # [G]-->[J]-->[I]-->[B]-->[C]-->[X]-->[Y]-->[Z]

    print('Length: %d' % len(ll))
    # Length: 8

    # ll.remove(20)
    ## this will raise error
    ## IndexError: linked list index out of range
