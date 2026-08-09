"""Excavation 134: make evidence and approval explicit."""

def accept(candidate):
    required = ("evidence", "failure_test", "approved")
    return all(candidate.get(key) for key in required)

if __name__ == "__main__":
    weak = {"evidence": True, "failure_test": False, "approved": True}
    repaired = {"evidence": True, "failure_test": True, "approved": True}
    assert not accept(weak)
    assert accept(repaired)
    print({"shortcut": accept(weak), "repair": accept(repaired)})
