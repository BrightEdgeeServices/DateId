test_set_01 = [
    ([2008, 1, 1], [2007, 12, 31], -1, -1),
    ([2008, 1, 1], [2008, 1, 1], 1, 1),
    ([2008, 1, 1], [2008, 1, 2], 2, 1),
    ([2008, 1, 1], [2007, 12, 1], -31, -1),
    ([2008, 1, 1], [2007, 11, 30], -32, -2),
    ([2008, 1, 1], [2008, 1, 31], 31, 1),
    ([2008, 1, 1], [2008, 2, 1], 32, 2),
]
test_set_02 = [
    ([2008, 1, 1], [2007, 12, 31], -1, -1),
    ([2008, 1, 1], [2008, 1, 1], 1, 1),
    ([2008, 1, 1], [2008, 1, 2], 2, 1),
    ([2008, 1, 1], [2007, 12, 1], -31, -1),
    ([2008, 1, 1], [2007, 11, 30], -32, -2),
    ([2008, 1, 1], [2008, 1, 31], 31, 1),
    ([2008, 1, 1], [2008, 2, 1], 32, 2),
]
test_set_03 = [
    ([2008, 1, 1], [2008, 1, 1], 0, 1),  # Test for day_id == 0
]

test_set_leap_years = [
    (2000, False),
    (2009, False),
    (2100, True),
    (2016, True),
]
