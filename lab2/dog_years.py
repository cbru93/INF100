def human_to_dog_years(human_years):
    if human_years <= 2:
        return human_years * 10.5 # First two years
    return 21 + (human_years - 2) * 4 # After two years


def almost_equals(a, b):
    return abs(a - b) < 0.00000001

def test_human_to_dog_years():
    print('Tester human_to_dog_years... ', end='')
    assert almost_equals(15.75, human_to_dog_years(1.5))
    assert almost_equals(21.00, human_to_dog_years(2))
    assert almost_equals(57.00, human_to_dog_years(11))
    print('OK')

test_human_to_dog_years()