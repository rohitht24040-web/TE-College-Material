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
                new_fact = True
                print("Derived:", conclusion)

        if not new_fact:
            break

    return facts


print("Initial Facts:", facts)

result = forward_chaining(facts, rules)

print("\nFinal Facts:", result)
