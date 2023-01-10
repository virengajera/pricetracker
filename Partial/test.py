@pytest.mark.parametrize("price, result",[
    ("7€",7.0),
    ("7,00€",7.0),
    ("7,23€",7.23),
    ("7.23€",723.0),
    ("7.090,55€",7090.55)
])
def test_formatPrice(price,result):
    assert scrap.formatPrice(price) == result 


@pytest.mark.parametrize("current, threshold, result",[
    (1,5,True),
    (1,1,True),
    (5,7,None)
])
def test_tracker(current, threshold, result):
    assert tracker_operations.tracker(current, threshold) == result


@pytest.mark.parametrize("link, result",[
    ("",False),
    (" ",False),
    ("0",False),
    ("https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#requesting-fixtures",False),
    ("https://www.amazon.de/-/en/SteelSeries-Keyboard-10-Zone-Lighting-Magnetic/dp/B083M9CBD5/ref=lp_193545031_1_1?th=1",True)
])
def test_isValidLink(link,result):
    assert validation.isValidLink(link) == result