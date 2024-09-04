import time

nemo = ['nemo']
everyone = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'nemo', 'Hannah', 'Ivy', 'Jack']
large = ["nemo"] * 1000000

def find_nemo (array):
    t0 = time.perf_counter()
    for i in range(len(array)):
        if array[i] == "nemo":
            print("Found nemo!!")
    t1 = time.perf_counter()
    print(f"Time taken {t1 - t0} milliseconds")

find_nemo(large)
