from doubly_linked_list import MyDoublyLinkedList


class MyQueue(object):

    def __init__(self, data_iter=None):
        self.__db_ll = MyDoublyLinkedList()
        if data_iter:
            for elem in data_iter:
                self.__db_ll.prepend(elem)

    def push(self, data):
        self.__db_ll.append(data)

    def pop(self):
        return self.__db_ll.pop()

    def __iter__(self):
        n = self.__db_ll.first
        while n:
            yield n.data
            n = n.next

    def __len__(self):
        return len(self.__db_ll)

    def __repr__(self):
        s = ''
        for n in self.__db_ll:
            s += '[%s]-->' % n.data
        return s.rstrip('-->')


if __name__ == '__main__':
    queue = MyQueue()

    queue.push('A')
    queue.push('B')
    queue.push('C')
    queue.push('D')

    for elem in queue:
        print(elem)
    # A
    # B
    # C
    # D

    print()
    print(queue)
    # [A]-->[B]-->[C]-->[D]

    print()
    print(f'Pop: {queue.pop()}')
    print(queue)
    # Pop: A
    # [B]-->[C]-->[D]

    print()
    print(f'Pop: {queue.pop()}')
    print(queue)
    # Pop: B
    # [C]-->[D]

    print()
    print(f'Length: {len(queue)}')
    # Length: 2
