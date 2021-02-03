#In this test we will ping to destination and count number which fetched from a csv file
import csv, subprocess, time
import datetime

csvFile="EnvVars.csv"
resFile="pingResFile.txt"
def readFile(fileName):#read csv file and return count and destination
    with open (csvFile) as file:
        reader=csv.reader(file,delimiter=',')
        line=0
        for row in reader:
            if line==0:
                line=+1
            else:
                count, destination =int(row[0]), row[1]
                print(count, destination)
                return count, destination

#function that will ping to the destination and count which fetched from the file

def pingToDest(destination, count, runNumber):
    subprocess.run('ping -n '+str(count)+ ' '+destination+ ' '+ '> '+ str(runNumber)+resFile, shell=True)

#Main:
runNumber=0
loopNumber=3
while runNumber<loopNumber:
    print("Starting the ping test...")
    values=readFile(csvFile)
    count=values[0]
    destination=values[1]
    print(count, destination)
    pingToDest(destination, count, runNumber)
    time.sleep(1.5)
    print("Finish ping test iteration!")
    runNumber+=1
