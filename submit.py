from parser import *
from solve import *


if __name__ == "__main__":
    problem = parse("data/kittens.in")
    solution = Solution(problem, solve1(problem))
    solution.verify_assignement()
    f = open("submission.txt", "w")
    f.write(solution.submission())
    f.close()