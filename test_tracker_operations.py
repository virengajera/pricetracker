import pytest
import tracker_operations

@pytest.mark.parametrize("current, threshold, result",[
    (1,5,True),
    (1,1,True),
    (5,7,None)
])
def test_tracker(current, threshold, result):
    assert tracker_operations.tracker(current, threshold) == result