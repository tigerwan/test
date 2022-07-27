"""
The Pool class represents a pool of worker processes
"""
from multiprocessing import Pool
from time import sleep
from datetime import datetime

def f(x):
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print('++++++pool.map++++++')
        print(pool.map(f, range(10)))


        # print same numbers in arbitrary order
        print('++++++pool.imap_unordered++++++')
        for i in pool.imap_unordered(f, range(10)):
            print(i)

        # evaluate "f(10)" asynchronously
        print('++++++pool.apply_async++++++')
        res = pool.apply_async(f, [10])
        print(res.get(timeout=1))             # prints "100"

        # make worker sleep for 10 secs
        print('++++++pool.apply_async, sleep 10 sec++++++')
        res = pool.apply_async(sleep, [10])
        # print(res.get(timeout=1))             # raises multiprocessing.TimeoutError

        print('++++++pool.join++++++')
        print('waitting star time:', datetime.now())
        pool.close()
        pool.join()
        print('waitting end time:', datetime.now())

    # exiting the 'with'-block has stopped the pool
