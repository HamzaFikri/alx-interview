#!/usr/bin/python3
"""
Print combinations of n-queens
"""
import sys

def solve_queens(n):
    """Solve queens using backtracking"""
    solution = []
    solve(0, n, solution)
    
def solve(row, n, solution):
    """Recursive function to solve queens"""
    if row == n:
        print_solution(solution)
    else:
        for col in range(n):
            if is_valid_placement(solution, row, col):
                solution.append((row, col))
                solve(row + 1, n, solution)
                solution.pop()

def is_valid_placement(solution, row, col):
    """Check if position is valid using symmetry property"""
    for queen in solution:
        if queen[1] == col or queen[0] + queen[1] == row + col or queen[0] - queen[1] == row - col:
            return False
    return True

def print_solution(solution):
    """Print the solution"""
    for queen in solution:
        print(queen)
    print()

if __name__ == "__main__":
    """Main"""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solve_queens(n)
