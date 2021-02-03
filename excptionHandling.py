#Make an informative message and print it instead of crashing!

def openFile(path):
    try:
        file=open(path, 'r')
        file.read()
    except:
        print("File was not found!!!!")



def splitNumber(number):
    try:
        print(number/2)
    except:
        print("an error acour, changing the input to intiger!")
        print(int(number)/2)

openFile('c:/www.csv')
number=input('please insert a number')
splitNumber(number)