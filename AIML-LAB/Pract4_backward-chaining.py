facts = {"fever", "cough"}

rules = [
    ({"fever", "cough"}, "flu"),
    ({"flu"}, "take_rest"),
    ({"flu"}, "consult_doctor")
]

def backward_chaining(goal, facts, rules):
    if goal in facts:
        return True

    for conditions, conclusion in rules:
        if conclusion == goal:
            for condition in conditions:
                if not backward_chaining(condition, facts, rules):
                    return False
            return True

    return False


goal = input("Enter goal: ")

if backward_chaining(goal, facts, rules):
    print(goal, "can be proved")
else:
    print(goal, "cannot be proved")
