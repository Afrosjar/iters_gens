class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor = 0
        self.cursor1 = 0
        return self

    def __next__(self):
        if self.cursor >= len(self.list_of_list):
            raise StopIteration
        if self.cursor1 >= len(self.list_of_list[self.cursor]):
            raise StopIteration
        item = self.list_of_list[self.cursor][self.cursor1]
        if isinstance(item, list):
            for i in FlatIterator(item):
                self.cursor1 += 1

                if self.cursor1 == len(self.list_of_list[self.cursor]:
                    self.cursor += 1
                    self.cursor1 = 0

                return i

        self.cursor1 += 1
        if self.cursor1 == len(self.list_of_list[self.cursor]):
            self.cursor += 1
            self.cursor1 = 0

        return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for item in FlatIterator(list_of_lists_2):
        print(item)
    # test_3()