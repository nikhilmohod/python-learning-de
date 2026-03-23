print("multi threding")

import time
import random
from concurrent.futures import ThreadPoolExecutor


def basic_fun(i):
    wait  =  random.randint(1,10)
    time.sleep(wait)
    print(f"time taken by process {i} : {wait}")

def basic_fun2(i,count):
    wait  =  random.randint(1,10)
    wait = wait + count
    time.sleep(wait)
    return f"time taken by process {i} : {wait}"
    
data = ["data-1","data-2","data-3","data-4"]
# for index, val in enumerate(data):
#     basic_fun(val,index)


with ThreadPoolExecutor(max_workers=len(data)) as executor:
    #  futures = executor.map(basic_fun,data) all simutenuosly

    futures_submit = [executor.submit(basic_fun2, val, idx) for idx, val in enumerate(data)] in paralle
    
    # Results milvanyathi (optional)
    results = [f.result() for f in futures_submit]  # required return
    print(f"results :{results}")




