
from turtle import reset
import pytest
'''
🧠 What is pytest.mark?

👉 pytest.mark is used to TAG tests

Think of it like putting labels on your tests.

Example labels:

smoke

regression

slow

api

login

'''
#Giving the parameters ,so it manual test case

@pytest.mark.parametrize("a,b,res",[(1,2,3),(3,4,7)])
def test_add(a,b,res):
    print(a+b)
    assert a+b==res

#running smoke test -- "python -m smoke"

@pytest.mark.smoke
def test_smoke():
    assert True

@pytest.mark.smoke
def test_smoke1():
    assert True

'''
🎓 Exam / Viva One-Liner (IMPORTANT)

pytest.mark is used to label test cases, and pytest.mark.smoke is a custom marker used to identify basic critical tests.

🧠 Easy way to remember

pytest.mark = tag
smoke = name of the tag
'''

#running or skipping the value - python -m skip
@pytest.mark.skip(reason="Not ready")
def test_skip():
    pass
