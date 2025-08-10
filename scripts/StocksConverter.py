import pandas as pd
import os 
import subprocess
import Variables
import time
from pynput.keyboard import Key, Controller

def startfile():
    os.startfile('Stocks.xlsx')
    time.sleep(3)
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('s')
        keyboard.release('s')
        time.sleep(1)
startfile()
time.sleep(3.5)

read_file = pd.read_excel ("Stocks.xlsx")
read_file.to_csv ("Stocks.csv", 
                  index = None,
                  header=True)
df = pd.DataFrame(pd.read_csv("Stocks.csv"))
df

#.BAT FILE 4 
file = 'Basic Auth Process Script4.bat'
#Get Balance Sheet Path
mainpath = os.getcwd()
file_name = f'Stocks.csv'
path = os.path.join(mainpath, file_name)
#Define Text Variables
text = f'set FileName="Stocks.csv"'
text2 = f'set FilePath="{path}"'
#Get Raw Bat4 File Path
file_name2 = 'Basic Auth Process Script.bat4'
with open(file,'r') as f:
        get_all=f.readlines()
        with open(file,'w') as f:
            for i,line in enumerate(get_all,1):           
                if i == 6:                             
                    f.writelines(f"{text}\n")
                else:
                    f.writelines(line)
with open(file,'r') as f:
    get_all=f.readlines()
    with open(file,'w') as f:
        for i,line in enumerate(get_all,1):           
            if i == 7:                             
                f.writelines(f"{text2}\n")
            else:
                f.writelines(line)
    f.close()

#Open Bat 4
subprocess.Popen(["start", "cmd", "/k", Variables.bat4], shell = True)
