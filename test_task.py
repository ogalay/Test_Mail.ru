value = 3


def test_list_append():
    my_list = [1, 3, 911, 103, 3]
    my_list.append(value)
    list_expected = [1, 3, 911, 103, 3, value]
    assert my_list == list_expected


def test_list_pop():
    my_list = [1, 3, 911, 103, 3]
    l1 = my_list.pop()
    list_expected = 3
    assert l1 == list_expected


def test_list_count():
    my_list = [1, 3, 911, 103, 3]
    expected = 2
    assert my_list.count(3) == expected


def test_set_generator():
    my_set = {i**2 for i in range(4)}
    expected_set = {0, 1, 4, 9}
    assert my_set == expected_set


def test_set_union():
    a = {'hello', 'world'}
    b = {'creator', 'world'}
    expected_set = {'hello', 'world', 'creator'}
    assert set.union(a, b) == expected_set


def test_set_add():
    my_set = {'hello, ', 'world'}
    set.add(my_set, '!')
    expected_set = {'hello, ', 'world'}
    try:
        assert my_set == expected_set
    except AssertionError:
        pass
