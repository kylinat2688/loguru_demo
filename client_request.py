import requests
from multiprocessing.dummy import Pool


def write_log(num):
    requests.get('http://127.0.0.1:7411/write_log')


with Pool(5) as pool:
    pool.map(write_log, range(100000000))
