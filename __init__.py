from dummyDFChecker import DummyDFChecker
from environmentConst import EnvironmentConst

def register(linter):
    linter.register_checker(EnvironmentConst(linter))
    linter.register_checker(DummyDFChecker(linter))