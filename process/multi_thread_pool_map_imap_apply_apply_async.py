"""
             Multi-args   Concurrence    Blocking     Ordered-results
map          no           yes            yes          yes
apply        yes          no             yes          no
map_async    no           yes            no           yes
apply_async  yes          yes            no           no
"""


from multiprocessing.dummy import Pool as ThreadPool
import threading
import time

def worker1(args):
    print('sleep 1s')
    time.sleep(1)
    print('worker1:{}:{}'.format(threading.currentThread().name, args))
    return args

def worker2(*args):
    print('sleep 1s')
    time.sleep(1)
    print('worker2:{}:{}'.format(threading.currentThread().name, args))
    return args

pool = ThreadPool(3)

# map
print('test map!!!')
results = pool.map(worker1, [1, 2, 3])
print('map result:{}'.format(results))

# apply
print('test apply!!!')
for x, y in [[1, 1], [2, 2]]:
    result = pool.apply(worker2, (x, y))
    print('apply result:{}'.format(result))
    results.append(result)


def collect_result(result):
    print('callback results:{}'.format(result))
    results.append(result)

# map_async
print('test map_async!!!')
pool.map_async(worker1, list(range(2)), callback=collect_result)

# apply_async
print('test apply_sync!!!')
for x, y in [[1, 1], [2, 2]]:
    pool.apply_async(worker2, (x, y), callback=collect_result)

pool.close()
pool.join()
