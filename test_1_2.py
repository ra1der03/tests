import pytest
from popular_names import mentors, popular_names

expected1 = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'


@pytest.mark.parametrize(
    'mentors_,expected_',
    [(mentors, expected1)])
def test_resulting(mentors_, expected_):
    result = popular_names(mentors_)
    assert result == expected_




