from library import calculate_fine


def test_no_fine_for_on_time_return():
    assert calculate_fine(0) == 0


def test_fine_for_late_return():
    assert calculate_fine(3) == 15


def test_fine_for_five_late_days():
    assert calculate_fine(5) == 25


def test_negative_days():
    try:
        calculate_fine(-1)
        assert False
    except ValueError:
        assert True