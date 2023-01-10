import pytest
import db_operations
import json

def test_read_db():
    assert type(db_operations.read_db()) ==  type({type:'str'})
    assert db_operations.read_db() ==  " "