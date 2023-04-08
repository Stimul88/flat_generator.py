class FlatIterator:

    def __init__(self, list_):
        self.list_ = list_
        self.cursor = -1

    def __iter__(self):

        self.cursor += 1
        self.nested_cursor = 0
        return self

    def __next__(self):
        if self.nested_cursor >= len(self.list_[self.cursor]):
            iter(self)
        if self.cursor >= len(self.list_):
            raise StopIteration
        self.nested_cursor += 1
        return self.list_[self.cursor][self.nested_cursor - 1]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    flatIterator = FlatIterator(list_of_lists_1)
    for item in flatIterator:
        print(item)

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]



if __name__ == '__main__':
    test_1()

    #
    # class FlatIterator:
    #
    #     def __init__(self, list_):
    #         self.list_ = list_
    #         self.cursor = -1
    #         self.list_len = len(self.list_)
    #
    #     def __iter__(self):
    #         self.cursor += 1
    #         self.nested_cursor = 0
    #         return self
    #
    #     def __next__(self):
    #         if self.nested_cursor >= len(self.list_[self.cursor]):
    #             iter(self)
    #         if self.cursor >= self.list_len:
    #             raise StopIteration
    #         self.nested_cursor += 1
    #         return self.list_[self.cursor][self.nested_cursor - 1]
