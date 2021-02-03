#ping to destination number of times after reading and using csv as input
import csv, time, subprocess
count=0
destination=0
csvFile='EnvVars.csv'
resFile='pingRes.txt'

#Function to read details from csv
def readFromCsv(csvFileName):
    with open (csvFileName) as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        line=0
        for row in reader:
            if line==0:
                line+=1
                pass
            else:
                count, destination = int(row[0]), row[1]
                print("count:", count)
                print("destination:", destination)
                return count, destination

#function which ping to the given cesination using the count and runNumber
def sendPing(destination, count, runNumber):
    # subprocess.run('ping -n '+str(count)+ ' '+destination+ ' '+ '>'+str(runNumber)+'pingRes.text', shell=True)
    subprocess.run('ping -n '+ str(count) + ' '+ destination + ' > ' +str(runNumber) + resFile, shell=True)

############################################################################################################
#Main:
runNumber=0
loop_times=2
while runNumber<loop_times:
    print("Starting with ping test...")
    vars=readFromCsv(csvFile)
    count=vars[0]
    destination=vars[1]
    print('count is:{}'.format(count))
    print('destination is:{}'.format(destination))
    sendPing(destination, count, runNumber)
    print('Finish with the pint test iteration')
    time.sleep(3)
    runNumber+=1