# Logic-Based AI in Python
**Introduction**

This notebook shows how to use basic logic operations in Python. We will create logic functions, evaluate logical statements, extend logic to work with predicates (conditions for sets of values), and build a simple AI agent that makes decisions based on its environment.
#Task 1: Propositional Logic Operations
# AND (∧): Logical conjunction
# This function returns True if both a and b are True, otherwise False.
def and_operation(p, q):
    return p and q

# OR (∨): Logical disjunction
# This function returns True if either a or c is True, otherwise False.
def or_operation(p, r):
    return p or r

# NOT (¬): Logical negation
# This function returns True if c is False, and False if c is True.
def not_operation(r):
    return not r

# IMPLIES (→): Logical implication
# This function returns True unless a is True and c is False (i.e., a → c is equivalent to ¬a ∨ c).
def implies_operation(p, r):
    return not p or r

# Testing the operations with sample values
p, q, r = True, True, False
and_result = and_operation(p, q)
or_result = or_operation(p, r)
not_result = not_operation(r)
implies_result = implies_operation(p, r)

# Print the results of logical operations
print(and_result, or_result, not_result, implies_result)

**Explanation**: This code performs basic logical operations like AND, OR, NOT, and IMPLIES. We test these operations with some example values.
#Task 2: Evaluate Logical Statements:

# This function evaluates a propositional logic statement given the truth values of the propositions.
# Parameters:
# - statement: A string representing the logical expression (e.g., "p and q").
# - values: A dictionary where the keys are proposition names and the values are their truth values.
def evaluate(statement, values):
    return eval(statement, {}, values)

# Example: Evaluating logical statements with predefined truth values
values = {'p': True, 'q': False, 'r': True}

# Define example statements to evaluate
statement_1 = "p and q"      # Expected: False
statement_2 = "p or q"       # Expected: True
statement_3 = "not r"        # Expected: False
statement_4 = "p and (not q)"  # Expected: True

# Evaluate and print results
eval_1 = evaluate(statement_1, values)
eval_2 = evaluate(statement_2, values)
eval_3 = evaluate(statement_3, values)
eval_4 = evaluate(statement_4, values)

print(eval_1, eval_2, eval_3, eval_4)

**Explanation**: This function checks if a logical statement is True or False based on the values of p, q, and r. We evaluate some example expressions.
#Task 3: Extend to Predicate Logic:
# Universal Quantifier (FOR ALL ∀)
# This function checks if a predicate is True for all elements in a given domain.
# Parameters:
# - predicate: A function that returns True or False for an element of the domain.
# - domain: A list of elements to check.
def forall(predicate, domain):
    return all(predicate(x) for x in domain)

# Existential Quantifier (EXISTS ∃)
# This function checks if a predicate is True for at least one element in a given domain.
# Parameters:
# - predicate: A function that returns True or False for an element of the domain.
# - domain: A list of elements to check.
def exists(predicate, domain):
    return any(predicate(x) for x in domain)

# Example predicates and domains
domain = [1, 2, 3, 4, 5]

# Predicate to check if a number is even
predicate_even = lambda x: x % 2 == 0
# Predicate to check if a number is positive
predicate_positive = lambda x: x > 0

# Apply quantifiers to the domain
forall_result = forall(predicate_even, domain)  # Expected: False (not all numbers are even)
exists_result = exists(predicate_even, domain)  # Expected: True (there are even numbers)

# Print the results of the quantifiers
print(forall_result, exists_result)

**Explanation**: We use two logic functions to check if a condition (e.g., being an even number) applies to all values or just some values in a list.


#Task 4: AI Agent Development:
# This function defines the behavior of a simple AI agent that makes decisions based on the environment.
# The agent will decide to "proceed" if the environment is safe and resources are available.
# Parameters:
# - environment: A dictionary containing environmental conditions like 'safe' and 'resources_available'.
def ai_agent(environment):
    return and_operation(environment['safe'], environment['resources_available'])

# Define the environment's state for the AI agent
environment = {
    'safe': True,
    'resources_available': False
}

# Make a decision based on the environment
decision = ai_agent(environment)

# Print the agent's decision
print("Decision to proceed:", decision)

**Explanation**: This is a simple AI agent that decides whether to proceed with an action based on two conditions: the environment is safe, and resources are available.
#Testing Different Scenarios
# Test the AI agent with different environments
environment_1 = {'safe': True, 'resources_available': True}
environment_2 = {'safe': True, 'resources_available': False}
environment_3 = {'safe': False, 'resources_available': True}

decision_1 = ai_agent(environment_1)  # Expected: True
decision_2 = ai_agent(environment_2)  # Expected: False
decision_3 = ai_agent(environment_3)  # Expected: False

print("Decision with environment_1:", decision_1)
print("Decision with environment_2:", decision_2)
print("Decision with environment_3:", decision_3)
