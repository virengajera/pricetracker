import pytest
import scrap

@pytest.mark.parametrize("price, result",[
    ("7€",7.0),
    ("7,00€",7.0),
    ("7,23€",7.23),
    ("7.23€",723.0),
    ("7.090,55€",7090.55)
])
def test_formatPrice(price,result):
    assert scrap.formatPrice(price) == result