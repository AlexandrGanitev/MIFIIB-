import subprocess
import os
import multiprocessing
import sys

nrange = "192.168.1."

for i in range(1, 254):
    address = nrange + str(i)
    res = subprocess.call(['fping', '-a', '-q', address])
    print(res)