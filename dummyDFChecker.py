from os import path
import astroid
import re 
from pylint import checkers, interfaces
from pylint.checkers import utils

DUMMY_DF_REGEX = "/$|([0-9]+?$)|dummy|^ignored_|^unused_"


class DummyDFChecker(checkers.BaseChecker):
    __implements__ = (interfaces.IAstroidChecker,)

    name = "dummy-df-checker"

    msgs = {
        "E3344": (
            "Avoid using dummy DF Names",
            "avoid-dummy-df",
            "Avoid numered df name like df_1, df1 or just df",
        )
    }

    def visit_name(self, node):  
        if re.search(DUMMY_DF_REGEX, node.name) : 
                    self.add_message(
                        'avoid-dummy-df', node=node,
                    )

    def visit_const(self, node): 
        if isinstance(node.parent, astroid.Assign): 
            for item in node.parent.targets: 
                if isinstance(item, astroid.AssignName):
                    if re.search(DUMMY_DF_REGEX, item.name) : 
                        self.add_message(
                            'avoid-dummy-df', node=node,
                        )
 
         

 
 

 
#def register(linter):
#    linter.register_checker(DummyDFChecker(linter))