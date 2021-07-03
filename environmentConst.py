import astroid
import re  
from pylint import checkers, interfaces
from pylint.checkers import utils

PROD_ENV_REGEX = "data_lake"


class EnvironmentConst(checkers.BaseChecker):
    __implements__ = (interfaces.IAstroidChecker,)

    name = "envoriment-const"

    msgs = {
        "E3345": (
            "No Envoriment Const",
            "no-envoriment-const",
            "using a envoriment const like ROOT_DIR or ENV to easy change dev and prod script  ",
        ),
        "E3346": (
            "Hard Code Envoriment",
            "hard-code-envoriment",
            "Use a envoriment const like ROOT_DIR or ENV and avoid use hard code to set the envoriment  ",
        )
    }
    def __init__(self, linter=None):
        super(EnvironmentConst, self).__init__(linter)
        self._env_vars = []
        self._first_const = []

    def visit_const(self, node): 
        if not self._first_const :
            self._first_const = node

        if isinstance(node.parent, astroid.Assign): 
            for item in node.parent.targets: 
                if isinstance(item, astroid.AssignName):
                    if item.name == "ROOT_DIR" or item.name == "ENV" :
                        self._env_vars = node 
                    else : 
                        if re.search(PROD_ENV_REGEX, node.value) :
                            self.add_message(
                                'hard-code-envoriment', node=node,
                            )

  
    def close(self): 
        if not self._env_vars  :
            self.add_message(  'no-envoriment-const', node=self._first_const )
 
#def register(linter):
#    linter.register_checker(EnvironmentConst(linter))