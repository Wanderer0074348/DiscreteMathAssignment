import itertools

def nonnegative_integer_solutions(k, n):
    # Generate all combinations of k nonnegative integers that sum up to n
    combinations = itertools.combinations_with_replacement(range(n+1), k)
    
    # Filter out the combinations that sum up to n
    solutions = [comb for comb in combinations if sum(comb) == n]
    
    return solutions

# Example usage
k = 5
n = 5
solutions = nonnegative_integer_solutions(k, n)
#printing them  in format x1+x2+xk=n
for sol in solutions:
    print(' + '.join([str(x) for x in sol]) + ' = ' + str(n))
