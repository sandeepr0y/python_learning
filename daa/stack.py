from doubly_linked_list import MyDoublyLinkedList


class MyStack(object):

    def __init__(self, data_iter=None):
        self.__db_ll = MyDoublyLinkedList(data_iter)

    def push(self, data):
        self.__db_ll.append(data)

    def pop(self):
        return self.__db_ll.pop_last()

    def __iter__(self):
        n = self.__db_ll.last
        while n:
            yield n.data
            n = n.prev

    def __len__(self):
        return len(self.__db_ll)

    def __repr__(self):
        s = ''
        for n in self.__db_ll:
            s += '[%s]<--' % n.data
        return s.rstrip('<--')


if __name__ == '__main__':
    stack = MyStack()

    stack.push('A')
    stack.push('B')
    stack.push('C')
    stack.push('D')

    for elem in stack:
        print(elem)
    # D
    # C
    # B
    # A

    print()
    print(stack)
    # [A]<--[B]<--[C]<--[D]

    print()
    print(f'Pop: {stack.pop()}')
    print(stack)
    # Pop: D
    # [A]<--[B]<--[C]

    print()
    print(f'Pop: {stack.pop()}')
    print(stack)
    # Pop: C
    # [A]<--[B]

    print()
    print(f'Length: {len(stack)}')
    # Length: 2
