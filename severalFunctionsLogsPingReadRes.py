import time, datetime, subprocess, csv
logFile='generalLogFile.txt'
sourceFile='EnvVars.csv'
resFile='pingRes.txt'

###################################################################################
#Function1 which write to log file
def write2Log(destFile, textToWrite):
    f=open(logFile, 'a')
    timestemp=str(datetime.datetime.now())
    f.write(timestemp + ' '+ textToWrite +'\n')
    f.close()
###############################################################################
#Function2 which read csv file (should print to log all actions!)

def readCsv(file):
    write2Log(logFile, 'Start to read the csv file')
    with open (sourceFile) as csvFile:
        reader=csv.reader(csvFile, delimiter=',')
        line=0
        for row in reader:
            if line==0:
                line+=1
            else:
                count, destination =str(row[0]), row[1]
                return count, destination
            write2Log(logFile, 'Finish reading the csv file')

###################################################################################
#Function3 which ping to destination after getting the return from function2
def ping2dest(destination, count, runNumber):
    write2Log(logFile, 'Start ping process'+ destination)
    subprocess.run('ping -n '+str(count)+ ' '+destination+ ' '+ '> '+ str(runNumber)+resFile, shell=True)
    write2Log(logFile, 'Finish pinging to'+ destination)
    return str(runNumber)+resFile
##############################################################################

#Function4 - check results
def checkRes(resFile):
    write2Log(logFile, 'checking res file')
    f=open(resFile, 'r')
    pingResults=f.read()
    if "Reply from 127.0.0.1: bytes=32 time<1ms TTL=128" in pingResults:
        write2Log(logFile, "ping to "+ destination + " PASS!!!")
        print("Ping test Pass!")

    else:
        write2Log(logFile, "ping to " + destination + " FAIL!!!")
        print("ping to "+destination+ "failed!!!")
    f.close()

##############################################################################

#Main:
runNumber=0
loopNumber=2
while runNumber<loopNumber:
    print("Starting the ping test...")
    vars=readCsv(sourceFile)
    count=vars[0]
    destination=vars[1]
    print(count, destination)
    ping2dest(destination, count, runNumber)
    print('ping test finish')
    time.sleep(2)

    runNumber+=1