import pytest
import validation

@pytest.mark.parametrize("link, result",[
    ("",False),
    (" ",False),
    ("0",False),
    ("https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#requesting-fixtures",False),
    ("https://www.amazon.de/-/en/SteelSeries-Keyboard-10-Zone-Lighting-Magnetic/dp/B083M9CBD5/ref=lp_193545031_1_1?th=1",True)
])
def test_isValidLink(link,result):
    assert validation.isValidLink(link) == result
    


    
    