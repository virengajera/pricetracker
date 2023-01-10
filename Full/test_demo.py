import pytest
import app

def test_read_db():
    assert app.read_db() == {};


def test_isValidLink():
    assert app.isValidLink('https://afsfs') == True;
    assert app.isValidLink(1) == False; 
    assert app.isValidLink('1') == False; #if input is given 1 then expected output is equal to False
    assert app.isValidLink(50) >= 66; #if input is given 5 then expected output is greater or equal to 66
    #other operator can be used are like: !=, > , < , <=
    # for string u can e.g type("hello") is str
    # e.g. "Hel" in "Hello String" or "Hell" not in "Hello String"


""" for iterating over multiple test cases """
@pytest.mark.parametrize("Num1 , Num2 , Result",[
    (7,3,10),
    ("Hello","World","Hello World"),
    (10.5,25.5,36)
])
def test_add(Num1,Num2,Result):
    """ Run the code with normal command will also work """
    assert app.sum(Num1,Num2) == Result

""" python -m pytest file.py --> to run pytest code """
""" pytest -v -s  for fixture images https://www.youtube.com/watch?v=JJmTO95AoqE&list=PLS1QulWo1RIaNFUz4zrztWlCJgkpXht-H&index=4&ab_channel=ProgrammingKnowledge """

