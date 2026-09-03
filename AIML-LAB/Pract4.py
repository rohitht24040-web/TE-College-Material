facts = {"fever", "cough"}

rules = [
    ({"fever", "cough"}, "flu"),
    ({"flu"}, "take_rest"),
    ({"flu"}, "consult_doctor")
]


def forward_chaining(facts, rules):
    facts = set(facts)

    while True:
        new_fact = False

        for conditions, conclusion in rules:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                print("Derived:", conclusion)
                new_fact = True

        if not new_fact:
            break

    print("Final Facts:", facts)


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


while True:
    print("\n--- Expert System ---")
    print("1. Forward Chaining")
    print("2. Backward Chaining")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nInitial Facts:", facts)
        forward_chaining(facts, rules)

    elif choice == 2:
        goal = input("Enter goal: ")

        if backward_chaining(goal, facts, rules):
            print(goal, "can be proved")
        else:
            print(goal, "cannot be proved")

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
