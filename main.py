import time

import solutions.day1.part1 as solDay1P1
import solutions.day1.part2 as solDay1P2
import solutions.day2.part1 as solDay2P1
import solutions.day2.part2 as solDay2P2
import solutions.day3.part1 as solDay3P1
import solutions.day3.part2 as solDay3P2
import solutions.day4.part1 as solDay4P1
import solutions.day4.part2 as solDay4P2
from solutions.solution import AbstractSolution


def main():
    run_verbose(solDay1P1.Part1())
    run_verbose(solDay1P2.Part2())
    run_verbose(solDay2P1.Part1())
    run_verbose(solDay2P2.Part2())
    run_verbose(solDay3P1.Part1())
    run_verbose(solDay3P2.Part2())
    run_verbose(solDay4P1.Part1())
    run_verbose(solDay4P2.Part2())
    run_verbose_benchmark(solDay4P2.Part2(), 100.0)


def run_verbose(sol: AbstractSolution):
    sTime = time.time()
    print(sol.get_description(), ": Result: ", sol.run(), ", Benchmark: ", time.time() - sTime)

def run_verbose_benchmark(sol: AbstractSolution, iterations: int):
    sTime = time.time()
    print("Running benchmark for "+sol.get_description())
    for i in range(0, int(iterations)):
        sol.run()
    print("avg time for ", iterations, " iterations: ", (time.time() - sTime)/iterations)

if __name__ == "__main__": main()
