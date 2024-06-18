import os
import csv
import fileinput
import sys
import csv
import subprocess
import Variables
import time

hardcodebalance = 'TSLA'
hardcodeincome = 'TSLA'
hardcodecash = 'TSLA'

#Stocks = ['MMM','A','AAL','AAP','AAPL','ABBV','ABC','ABMD','ABT','ACN','ADBE','ADI','ADM','ADP','ADSK','AEE','AEP','AES','AFL','AIG','AIZ','AJG','AKAM','ALB','ALGN','ALK','ALL','ALLE','AMAT','AMCR','AMD','AME','AMGN','AMP','AMT','AMZN','ANET','ANSS','ANTM','AON','AOS','APA','APD','APH','APTV','ARE','ATO','ATVI','AVB','AVGO','AVY','AWK','AXP','AZO','BA','BAC','BAX','BBWI','BBY','BDX','BEN','BF.B','BIIB','BIO','BK','BKNG','BKR','BLK','BLL','BMY','BR','BRK.B','BRO','BSX','BWA','BXP','C','CAG','CAH','CARR','CAT','CB','CBOE','CBRE','CCI','CCL','CDAY','CDNS','CDW','CE','CERN','CF','CFG','CHD','CHRW','CHTR','CI','CINF','CL','CLX','CMA','CMCSA','CME','CMG','CMI','CMS','CNC','CNP','COF','COO','COP','COST','CPB','CPRT','CRL','CRM','CSCO','CSX','CTAS','CTLT','CTRA','CTSH','CTVA','CTXS','CVS','CVX','CZR','D','DAL','DD','DE','DFS','DG','DGX','DHI','DHR','DIS','DISCA','DISCK','DISH','DLR','DLTR','DOV','DOW','DPZ','DRE','DRI','DTE','DUK','DVA','DVN','DXC','DXCM','EA','EBAY','ECL','ED','EFX','EIX','EL','EMN','EMR','ENPH','EOG','EQIX','EQR','ES','ESS','ETN','ETR','ETSY','EVRG','EW','EXC','EXPD','EXPE','EXR','F','FANG','FAST','FB','FBHS','FCX','FDX','FE','FFIV','FIS','FISV','FITB','FLT','FMC','FOX','FOXA','FRC','FRT','FTNT','FTV','GD','GE','GILD','GIS','GL','GLW','GM','GNRC','GOOG','GOOGL','GPC','GPN','GPS','GRMN','GS','GWW','HAL','HAS','HBAN','HBI','HCA','HD','HES','HIG','HII','HLT','HOLX','HON','HPE','HPQ','HRL','HSIC','HST','HSY','HUM','HWM','IBM','ICE','IDXX','IEX','IFF','ILMN','INCY','INFO','INTC','INTU','IP','IPG','IPGP','IQV','IR','IRM','ISRG','IT','ITW','IVZ','J','JBHT','JCI','JKHY','JNJ','JNPR','JPM','K','KEY','KEYS','KHC','KIM','KLAC','KMB','KMI','KMX','KO','KR','KSU','L','LDOS','LEG','LEN','LH','LHX','LIN','LKQ','LLY','LMT','LNC','LNT','LOW','LRCX','LUMN','LUV','LVS','LW','LYB','LYV','MA','MAA','MAR','MAS','MCD','MCHP','MCK','MCO','MDLZ','MDT','MET','MGM','MHK','MKC','MKTX','MLM','MMC','MNST','MO','MOS','MPC','MPWR','MRK','MRNA','MRO','MS','MSCI','MSFT','MSI','MTB','MTCH','MTD','MU','NCLH','NDAQ','NEE','NEM','NFLX','NI','NKE','NLOK','NLSN','NOC','NOW','NRG','NSC','NTAP','NTRS','NUE','NVDA','NVR','NWL','NWS','NWSA','NXPI','O','ODFL','OGN','OKE','OMC','ORCL','ORLY','OTIS','OXY','PAYC','PAYX','PBCT','PCAR','PEAK','PEG','PENN','PEP','PFE','PFG','PG','PGR','PH','PHM','PKG','PKI','PLD','PM','PNC','PNR','PNW','POOL','PPG','PPL','PRU','PSA','PSX','PTC','PVH','PWR','PXD','PYPL','QCOM','QRVO','RCL','RE','REG','REGN','RF','RHI','RJF','RL','RMD','ROK','ROL','ROP','ROST','RSG','RTX','SBAC','SBUX','SCHW','SEE','SHW','SIVB','SJM','SLB','SNA','SNPS','SO','SPG','SPGI','SRE','STE','STT','STX','STZ','SWK','SWKS','SYF','SYK','SYY','T','TAP','TDG','TDY','TECH','TEL','TER','TFC','TFX','TGT','TJX','TMO','TMUS','TPR','TRMB','TROW','TRV','TSCO','TSLA','TSN','TT','TTWO','TWTR','TXN','TXT','TYL','UA','UAA','UAL','UDR','UHS','ULTA','UNH','UNP','UPS','URI','USB','V','VFC','VIAC','VLO','VMC','VNO','VRSK','VRSN','VRTX','VTR','VTRS','VZ','WAB','WAT','WBA','WDC','WEC','WELL','WFC','WHR','WLTW','WM','WMB','WMT','WRB','WRK','WST','WU','WY','WYNN','XEL','XLNX','XOM','XRAY','XYL','YUM','ZBH','ZBRA','ZION','ZTS']


Stocks = ['APPL']

for i in Stocks:
    MainTicker = i
    def Ticker1():                  
        import requests
        Ticker = f"{MainTicker} Income Statement"
        res = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{MainTicker}?datatype=csv&apikey=5ea3b74b181fdc8c41bf6bd86d012274')
        open(Ticker + '.csv', 'wb').write(res.content)
    def Ticker2():
        import requests
        Ticker = f"{MainTicker} Cash Flow"
        res = requests.get(f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{MainTicker}?datatype=csv&apikey=5ea3b74b181fdc8c41bf6bd86d012274')
        open(Ticker + '.csv', 'wb').write(res.content)
    def Ticker3():
        import requests
        Ticker = f"{MainTicker} Balance Sheet"
        res = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{MainTicker}?datatype=csv&apikey=5ea3b74b181fdc8c41bf6bd86d012274')
        open(Ticker + '.csv', 'wb').write(res.content)
    Ticker1()
    Ticker2()
    Ticker3()

    #Retry Check
    file1 = f'{MainTicker} Income Statement.csv'
    file2 = f'{MainTicker} Cash Flow.csv'
    file3 = f'{MainTicker} Balance Sheet.csv'
    search_word = 'contact'
    with open(file1) as f:
        if search_word in f.read():
            Ticker1()
            print('REDONE Income Statement')
        else:
            print(f'{MainTicker} Income Statement Complete')
    with open(file2) as f:
        if search_word in f.read():
            Ticker2()
            print('REDONE Cash Flow')
        else:
            print(f'{MainTicker} Cash Flow Complete')
    with open(file3) as f:
        if search_word in f.read():
            Ticker3()
            print('REDONE Balance Sheet')
        else:
            print(f'{MainTicker} Balance Sheet Complete')

    #ReWrite Balance Sheet (.csv)
    input_file1 = f'{MainTicker} Balance Sheet.csv'
    output_file1 = f'{MainTicker} Balance Sheet New.csv'
    cols_to_remove = [0] 
    cols_to_remove = sorted(cols_to_remove, reverse=True) 
    row_count = 0 
    with open(input_file1, "r") as source:
        reader = csv.reader(source)
        with open(output_file1, "w", newline='') as result:
            writer = csv.writer(result)
            for row in reader:
                row_count += 1
                for col_index in cols_to_remove:
                    del row[col_index]
                writer.writerow(row)

    #Rewrite Cash Flow (.csv)
    input_file2 = f'{MainTicker} Cash Flow.csv'
    output_file2 = f'{MainTicker} Cash Flow New.csv'
    cols_to_remove = [0] 
    cols_to_remove = sorted(cols_to_remove, reverse=True) 
    row_count = 0 
    with open(input_file2, "r") as source:
        reader = csv.reader(source)
        with open(output_file2, "w", newline='') as result:
            writer = csv.writer(result)
            for row in reader:
                row_count += 1
                for col_index in cols_to_remove:
                    del row[col_index]
                writer.writerow(row)


    #ReWrite Balance Sheet (.csv)
    input_file1 = f'{MainTicker} Income Statement.csv'
    output_file1 = f'{MainTicker} Income Statement New.csv'
    cols_to_remove = [0] 
    cols_to_remove = sorted(cols_to_remove, reverse=True) 
    row_count = 0 
    with open(input_file1, "r") as source:
        reader = csv.reader(source)
        with open(output_file1, "w", newline='') as result:
            writer = csv.writer(result)
            for row in reader:
                row_count += 1
                for col_index in cols_to_remove:
                    del row[col_index]
                writer.writerow(row)

    #Add Ticker Column Balance Sheet
    input_file = f'{MainTicker} Balance Sheet New.csv'
    output_file = f'{MainTicker} Balance Sheet.csv'
    with open(input_file,'r') as csvinput:
        with open(output_file, 'w') as csvoutput:
                writer = csv.writer(csvoutput)
                for row in csv.reader(csvinput):
                    writer.writerow(row+[f'{MainTicker}'])
    os.remove(f'{MainTicker} Balance Sheet New.csv')

    #Add Ticker Column Cash Flow Sheet
    input_file = f'{MainTicker} Cash Flow New.csv'
    output_file = f'{MainTicker} Cash Flow.csv'
    with open(input_file,'r') as csvinput:
        with open(output_file, 'w') as csvoutput:
                writer = csv.writer(csvoutput)
                for row in csv.reader(csvinput):
                    writer.writerow(row+[f'{MainTicker}'])
    os.remove(f'{MainTicker} Cash Flow New.csv')

    #Add Ticker Column Income Statement
    input_file = f'{MainTicker} Income Statement New.csv'
    output_file = f'{MainTicker} Income Statement.csv'
    with open(input_file,'r') as csvinput:
        with open(output_file, 'w') as csvoutput:
                writer = csv.writer(csvoutput)
                for row in csv.reader(csvinput):
                    writer.writerow(row+[f'{MainTicker}'])
    os.remove(f'{MainTicker} Income Statement New.csv')

    #Add Ticker Name as Header
    for line in fileinput.input(f"{MainTicker} Balance Sheet.csv", inplace=1):
        if "FY" in line:
            line = line.replace(f"{MainTicker}", "Ticker:")
        sys.stdout.write(line)
    for line in fileinput.input(f"{MainTicker} Cash Flow.csv", inplace=1):
        if "FY" in line:
            line = line.replace(f"{MainTicker}", "Ticker:")
        sys.stdout.write(line)
    for line in fileinput.input(f"{MainTicker} Income Statement.csv", inplace=1):
        if "FY" in line:
            line = line.replace(f"{MainTicker}", "Ticker:")
        sys.stdout.write(line)

    #.BAT FILE 1 (Balance Sheet)
    file = 'Basic Auth Process Script.bat'
    #Get Balance Sheet Path
    mainpath = os.getcwd()
    file_name = f'{MainTicker} Balance Sheet.csv'
    path = os.path.join(mainpath, file_name)
    #Define Text Variables
    text = f'set FileName="{hardcodebalance} Balance Sheet.csv"'
    text2 = f'set FilePath="{path}"'
    #Get Raw Bat1 File Path
    file_name2 = 'Basic Auth Process Script.bat'
    path2 = os.path.join(mainpath, file_name2)
    with open(file,'r') as f:
        get_all=f.readlines()
        with open(file,'w') as f:
            for i,line in enumerate(get_all,1):           
                if i == 7:                             
                    f.writelines(f"{text2}\n")
                else:
                    f.writelines(line)
        f.close()
    
    #.BAT FILE 2 (Income Statement)
    file = 'Basic Auth Process Script2.bat'
    #Get Income Statement Path
    mainpath = os.getcwd()
    file_name = f'{MainTicker} Income Statement.csv'
    path = os.path.join(mainpath, file_name)
    #Define Text Variables
    text = f'set FileName="{hardcodeincome} Income Statement.csv"'
    text2 = f'set FilePath="{path}"'
    #Get Raw Bat2 File Path
    file_name2 = 'Basic Auth Process Script2.bat'
    path2 = os.path.join(mainpath, file_name2)
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

    #.BAT FILE 3 (Cash Flow)
    file = 'Basic Auth Process Script3.bat'
    #Get Income Statement Path
    mainpath = os.getcwd()
    file_name = f'{MainTicker} Cash Flow.csv'
    path = os.path.join(mainpath, file_name)
    #Define Text Variables
    text = f'set FileName="{hardcodecash} Cash Flow.csv"'
    text2 = f'set FilePath="{path}"'
    #Get Raw Bat2 File Path
    file_name2 = 'Basic Auth Process Script3.bat'
    path2 = os.path.join(mainpath, file_name2)
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
    
    #Open Bat1   
    subprocess.Popen(["start", "cmd", "/k", Variables.bat1], shell = True)
    time.sleep(5)
    
    #Open Bat2
    subprocess.Popen(["start", "cmd", "/k", Variables.bat2], shell = True)

    #Open Bat3
    subprocess.Popen(["start", "cmd", "/k", Variables.bat3], shell = True)
    
    time.sleep(9)
