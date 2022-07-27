"""
             Multi-args   Concurrence    Blocking     Ordered-results
map          no           yes            yes          yes
apply        yes          no             yes          no
map_async    no           yes            no           yes
apply_async  yes          yes            no           no
"""

from multiprocessing.dummy import Pool as ThreadPool
import time

def squareNumber(n):
    print('jump in squareNumber')
    return n ** 2

# function to be mapped over
def calculateParallel(numbers, threads=2):
    pool = ThreadPool(threads)
    results = pool.map(squareNumber, numbers)
    time.sleep(5)
    print('before close')
    pool.close()
    print('after close')
    pool.join()
    print('after join')
    return results

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    squaredNumbers = calculateParallel(numbers, 4)
    print(squaredNumbers)
    # for n in squaredNumbers:
    #    print(n)