# Task 1: Propositional Logic Operations

# AND (∧): Logical conjunction
# This function returns True if both a and b are True, otherwise False.
def and_operation(a, b):
    return a and b

# OR (∨): Logical disjunction
# This function returns True if either a or c is True, otherwise False.
def or_operation(a, c):
    return a or c

# NOT (¬): Logical negation
# This function returns True if c is False, and False if c is True.
def not_operation(c):
    return not c

# IMPLIES (→): Logical implication
# This function returns True unless a is True and c is False (i.e., a → c is equivalent to ¬a ∨ c).
def implies_operation(a, c):
    return not a or c

# Testing the operations with sample values
a, b, c = True, True, False
and_result = and_operation(a, b)
or_result = or_operation(a, c)
not_result = not_operation(c)
implies_result = implies_operation(a, c)

# Print the results of logical operations
print(and_result, or_result, not_result, implies_result)


# Task 2: Evaluate Logical Statements

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


# Task 3: Extend to Predicate Logic

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


# Task 4: AI Agent Development

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
