import os 
import time

def rundate():
    os.system('python TodayDateConverter.py')

def runstocks():
    os.system('python StocksConverter.py')

rundate()
time.sleep(7.5)
runstocks()