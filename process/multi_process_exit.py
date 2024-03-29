import multiprocessing
import sys
import time

def exit_error():
    sys.exit(1)

def exit_ok():
    return

def return_value():
    return 1

def raises():
    raise RuntimeError('There was an error!')

def terminated():
    time.sleep(3)

if __name__ == '__main__':
    jobs = []
    for f in [exit_error, exit_ok, return_value, raises, terminated]:
        print('Starting process for {}'.format(f.__name__))
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()
        
    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print('%s.exitcode = %s' % (j.name, j.exitcode))
