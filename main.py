import tracemalloc
import dpImplementation
import BnBImplementation
import time
import psutil  # For memory usage on Unix systems

def read_first_lines(filename, lines):
    with open(filename, "r") as file:
        lines = [next(file) for _ in range(lines)]
    return lines
 

def run_experiment(algorithm, inputfile, vertex):
    tracemalloc.start()
    start_time = time.time()
    algorithm(inputfile, vertex)
    memory_usage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, memory_usage

def main():
    # Generate datasets
    file_10000 = "10000_vertex.txt"
    file_100000 = "100000_vertex.txt"
    file_1000000 = "1000000_vertex.txt"

    dp_time_10000, dp_memory_10000 = run_experiment(dpImplementation.main, file_10000, 10000)
    bnb_time_60, bnb_memory_60 = run_experiment(BnBImplementation.main, file_10000, 60)

    dp_time_100000, dp_memory_100000= run_experiment(dpImplementation.main,file_100000, 100000)
    bnb_time_90, bnb_memory_90 = run_experiment(BnBImplementation.main, file_100000, 90)

    dp_time_1000000, dp_memory_1000000= run_experiment(dpImplementation.main, file_1000000, 100000)
    bnb_time_120, bnb_memory_120 = run_experiment(BnBImplementation.main, file_1000000, 120)


    print(f"BnB Time (Nodes: 60, Cutoff Time: 300s): {bnb_time_60}, BnB Memory: {bnb_memory_60}")
    print(f"DP Time (Nodes: 10000, Cutoff Time: None): {dp_time_10000}, DP Memory: {dp_memory_10000}")
    print(f"BnB Time (Nodes: 90, Cutoff Time: 300s): {bnb_time_90}, BnB Memory: {bnb_memory_90}")
    print(f"DP Time (Nodes: 100000, Cutoff Time: None): {dp_time_100000}, DP Memory: {dp_memory_100000}")
    print(f"BnB Time (Nodes: 120, Cutoff Time: 900s): {bnb_time_120}, BnB Memory: {bnb_memory_120}")
    print(f"DP Time (Nodes: 1000000, Cutoff Time: None): {dp_time_1000000}, DP Memory: {dp_memory_1000000}")


if __name__ == "__main__":
    main()
