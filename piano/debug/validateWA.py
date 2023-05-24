import filecmp
import os
if __name__ == '__main__':
    generator = "generator.py"
    solution = "../piano.py"  # change this to your solution
    bruteForce = "bruteforce.py"  # change this to your bruteforce solution
    iterations = 1000

    solutionOut = "solution.ans"
    bruteOut = "brute.ans"

    print(f"Running {iterations} iterations")
    for i in range(1, iterations):
        print(i)
        os.system(f"python3 {generator} > test.in")
        os.system(f"python3 {solution} < test.in > {solutionOut}")
        os.system(f"python3 {bruteForce} < test.in > {bruteOut}")
        if not filecmp.cmp(solutionOut, bruteOut):
            print("Error found")
            break