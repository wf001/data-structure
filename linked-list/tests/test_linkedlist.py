from src.linkedlist import LinkedList
import pytest


class TestLinkedList:
    @pytest.fixture
    def init(self):
        act = LinkedList()

        act.append(1)
        act.append(2)
        act.append(3)
        yield act

    def test_append(self, init):
        act = init
        assert len(act) == 3
        expect = [1, 2, 3]
        for i in range(3):
            assert act[i] == expect[i]

    def test_insert(self, init):
        act = init
        act.insert(4, 1)
        act.insert(5, 3)
        assert len(act) == 5
        expect = [1, 4, 2, 5, 3]
        for i in range(5):
            assert act[i] == expect[i]

    def test_pop_back(self, init):
        act = init
        act.pop_back()
        assert len(act) == 2
        expect = [1, 2]
        for i in range(2):
            assert act[i] == expect[i]

    def test_pop_front(self, init):
        act = init
        act.pop_front()
        assert len(act) == 2
        expect = [2, 3]
        for i in range(2):
            assert act[i] == expect[i]

    def test_iterate(self, init):
        act = init
        expect = [1, 2, 3]
        act_list = []
        for a in act:
            act_list.append(a)

        assert expect == act_list

    def test__setitem__(self, init):
        act = init
        expect = [3, 2, 3]
        act[0] = 3

        act_list = []
        for a in act:
            act_list.append(a)

        assert expect == act_list

    def test__add__(self, init):
        act = init
        lst2 = LinkedList()
        lst2.append(6)
        lst2.append(4)
        expect = [1, 2, 3, 6, 4]

        act = act+lst2

        act_list = []
        assert len(act) == 5
        for a in act:
            act_list.append(a)

        assert expect == act_list

    def test__add__(self):
        act = LinkedList()

        act.append(4)
        act.append(2)
        act.append(3)
        act.append(6)
        act.append(5)
        expect = [2, 3, 4, 5, 6]

        a = act.sorted()

        act_list = []
        assert len(a) == 5
        for ai in a:
            act_list.append(ai)

        assert expect == act_list
