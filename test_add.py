from add import add


def test_add():
    # arrange
    a = 1
    b = 2
    expect = 3

    # act
    result = add(a, b)

    # assert
    assert expect == result


def test_add_table_driver():
    # arrange
    params = [
        {
            "a": 1,
            "b": 6,
            "sum": 7
        },
        {
            "a": 2,
            "b": 7,
            "sum": 9
        }
    ]

    # act
    for item in params:
        expect = item['sum']
        result = add(item["a"], item["b"])
        # assert
        assert expect == result

