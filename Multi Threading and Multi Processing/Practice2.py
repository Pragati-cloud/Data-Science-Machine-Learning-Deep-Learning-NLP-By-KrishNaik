# process that run in parallel
#cpu bound 

import multiprocessing
import time

def square_num():
  for i in range(5):
    time.sleep(1)
    print(f"Square: {i*i}")


def cube_num():
  for i in range(5):
    time.sleep(1.5)
    print(f"Square: {i*i*i}")

if __name__=="__main__":

    #create 2 processes

    p1 = multiprocessing.Process(target=square_num)
    p2 = multiprocessing.Process(target=cube_num)
    t= time.time()

    ## start the process

    p1.start()
    p2.start()

    # wait process to complete

    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(finished_time)
