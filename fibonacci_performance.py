import sys
import tabulate
import time
import matplotlib.pyplot as plt

def fib(i):
    if i==0:
        return 1;
    elif i==1:
        return 1;
    else:
        return fib(i-1) + fib(i-2)


lookup_table = []
def dynamic_fib(i):
    global lookup_table
    if i==0:
        return 1;
    elif i==1:
        return 1;
    else:
        if lookup_table[i-1] != 0:
            fib1 = lookup_table[i-1]
        else:
            fib1 = dynamic_fib(i-1)
            lookup_table[i-1] = fib1

        if lookup_table[i-2] != 0:
            fib2 = lookup_table[i-2]
        else:
            fib2 = dynamic_fib(i-2)
            lookup_table[i-2] = fib2
        return fib1 + fib2

if __name__ == "__main__":
    fib_num = int(sys.argv[1])
    lookup_table = [0 for i in range(fib_num)]
    test_numbers = range(2, fib_num, 2)
    reg_fib_times = []
    dyn_fib_times = []

    for num in test_numbers:
        start = time.time()
        fib(num)
        end = time.time()
        reg_fib_times.append(end-start)
        
        start = time.time()
        dynamic_fib(num)
        end = time.time()
        dyn_fib_times.append(end-start)

    table = zip(test_numbers, reg_fib_times, dyn_fib_times)
    print(tabulate.tabulate(table, 
        headers=['Test Value', 'Plain Recursion Times', 'Dynamic Programming Times'], 
        tablefmt='pipe'))
    line1 = plt.plot(test_numbers, reg_fib_times, 'r--', label="Plain Recursion")
    line2 = plt.plot(test_numbers, dyn_fib_times, 'b--', label="Dynamic Programming")
    plt.legend(loc=0)

    plt.ylabel("Time (s)")
    plt.xlabel("Test Values")
    plt.title("Performance Comparison")
    plt.show()
