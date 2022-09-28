class Node:
    def __init__(self, _state, _parent=None, _action=None, _cost=0):
        self.state = _state
        self.parent = _parent
        self.action = _action
        self.cost = _cost

    def total_path(self):
    	if self.Parent is None:
    		return []
    	return self.parent.total_path() + [self.action]
        

    def __str__(self):
    	return super().__str__()+ 'Node: '+self.state + ' ' + self.parent+' parent:'


def test_robot():
    # For the problem of the robot cleaning two cells
    from collections import namedtuple
    State = namedtuple("State", "cell clean0 clean1")
    
    root = Node(State(0, False, False))
    step1 = Node(
        State(0, True, False),
        root, "SWEEP"
    )
    step2 = Node(
        State(1, True, False),
        step1, "MOVE"
    )
    step3_1 = Node(
        State(0, True, False),
        step2, "MOVE"
    )
    step3_2 = Node(
        State(1, True, True),
        step2, "SWEEP"
    )

    print(root)
    print(step1)
    print(step3_1.total_path())
    print(step3_2.total_path())


if __name__ == "__main__":
    test_robot()
