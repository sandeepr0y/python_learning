import numpy as np
from doubly_linked_list import MyDoublyLinkedList, Node


class HMDoublyLinkedList(MyDoublyLinkedList):

    def insert_after_value(self, data_after, data_to_insert):
        node_to_insert = Node(data_to_insert)
        for n in self:
            if n.data[1] == data_after:
                node_to_insert.next = n.next
                node_to_insert.prev = n
                if n.next is None:
                    self.last = node_to_insert
                else:
                    n.next.prev = node_to_insert
                n.next = node_to_insert
                break
        else:
            raise ValueError(f'value [{data_after}] not found in linked list')

    def remove_by_key(self, k):
        pre_node = None
        for n in self:
            if n.data[0] == k:
                if pre_node is None:
                    self.pop()
                else:
                    pre_node.next = n.next
                    if pre_node.next is None:
                        self.last = pre_node
                    else:
                        pre_node.next.prev = pre_node
                break
            pre_node = n
        else:
            raise ValueError(f'Key [{k}] not found in linked list')

    def remove_by_value(self, data):
        pre_node = None
        for n in self:
            if n.data[1] == data:
                if pre_node is None:
                    self.pop()
                else:
                    pre_node.next = n.next
                    if pre_node.next is None:
                        self.last = pre_node
                    else:
                        pre_node.next.prev = pre_node
                break
            pre_node = n
        else:
            raise ValueError(f'value [{data}] not found in linked list')

    def print_backwards(self):
        s = ''
        for n in reversed(self):
            s += '%s<-->' % str(n.data)
        print(s.rstrip('<-->'))
    
    def __repr__(self):
        s = ''
        for n in self:
            s += '%s<-->' % str(n.data)
        s = s.rstrip('<-->')
        return s if s else '()'


class MyHashMap(object):

    MAX_LENGTH = 10

    def __init__(self):
        self.key_set = set()
        self.arr = np.empty(self.MAX_LENGTH, dtype=HMDoublyLinkedList)

    def keys(self):
        return list(self.key_set)

    def values(self):
        return [v for k, v in self]

    def set(self, k, v):
        self[k] = v

    def get(self, k, default=None):
        try:
            return self[k]
        except KeyError:
            return default

    def remove(self, k):
        del self[k]

    @classmethod
    def __get_hash(cls, ss):
        ord_sum = 0
        for s in ss:
            ord_sum += ord(s)
        return ord_sum % cls.MAX_LENGTH

    def __setitem__(self, k, v):
        key_hash = self.__get_hash(k)
        ll = self.arr[key_hash] if self.arr[key_hash] else HMDoublyLinkedList()

        if k in self.key_set:
            # update
            for n in ll:
                if n.data[0] == k:
                    n.data = (k, v,)
                    break
            else:
                ll.append((k, v,))
        else:
            # insert
            ll.append((k, v,))
            self.key_set.add(k)

        self.arr[key_hash] = ll

    def __getitem__(self, k):
        if k not in self.key_set:
            raise KeyError(f'key [{k}] not found in MyHashMap')
        
        key_hash = self.__get_hash(k)
        ll = self.arr[key_hash]

        for n in ll:
            if n.data[0] == k:
                return n.data[1]

        raise KeyError(f'key [{k}] not found in MyHashMap')

    def __iter__(self):
        for ll in self.arr:
            if ll is not None:
                for n in ll:
                    yield n.data

    def __repr__(self):
        s = '{'
        for k, v in self:
            s += "'%s': %r, " % (k, v)
        s = s.rstrip(', ')
        s += '}'
        return s

    def __contains__(self, k):
        return k in self.key_set

    def __delitem__(self, k):
        if k not in self.key_set:
            raise KeyError(f'key [{k}] not found in MyHashMap')

        key_hash = self.__get_hash(k)
        ll = self.arr[key_hash]
        ll.remove_by_key(k)


if __name__ == '__main__':
    m = MyHashMap()

    m['name'] = 'Ramesh'
    m['age'] = 36
    m['gender'] = 'M'

    print(m['age'])
    # 36

    print(m)
    # {'age': 36, 'name': 'Ramesh', 'gender': 'M'}

    print('name' in m)
    # True

    print('post' in m)
    # False

    print(m.keys())
    # ['age', 'gender', 'name']

    print(m.values())
    # [36, 'Ramesh', 'M']

    print(m.get('name', 'NA'))
    # Ramesh

    print(m.get('last_name', 'NA'))
    # NA

    m['cars'] = MyHashMap()
    m['cars']['car-1'] = 'BMW'
    m['cars']['car-2'] = 'Audi'
    m['cars']['car-3'] = 'Ford'
    print(m)
    # {'age': 36, 'name': 'Ramesh', 'cars': {'car-1': 'BMW', 'car-2': 'Audi', 'car-3': 'Ford'}, 'gender': 'M'}

    m['cars'].remove('car-2')
    print(m)
    # {'age': 36, 'name': 'Ramesh', 'cars': {'car-1': 'BMW', 'car-3': 'Ford'}, 'gender': 'M'}

    del m['age']
    print(m)
    # {'name': 'Ramesh', 'cars': {'car-1': 'BMW', 'car-3': 'Ford'}, 'gender': 'M'}

    print('--------- Actual internal storage ----------')
    for idx, ele in enumerate(m.arr, start=0):
        print('[%d]: %s' % (idx, ele))
    # --------- Actual internal storage ----------
    # [0]: None
    # [1]: ()
    # [2]: None
    # [3]: None
    # [4]: None
    # [5]: ('cars', {'car-1': 'BMW', 'car-3': 'Ford'})
    # [6]: None
    # [7]: ('name', 'Ramesh')
    # [8]: None
    # [9]: ('gender', 'M')
