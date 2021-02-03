myList=['BMW', 'MAZDA', 'HYUNDAI', 'ferrari', 'lamborginy'] #task1
print("the list length is:", len(myList)) #task2

print(sorted(myList))#task3

print("The 3rd car is:", myList[2]) #task4

myList[1]="testCar" #task5
print(myList)
myList.append('addedCar')#task6
print(myList)
myList.pop(2) #task7
print(myList)

car=input("please insert a car name...")
if car in myList:
    print("the producer,"+ car+ " you are looking for is located in index:",myList.index(car)+1)
    print('The car brand is: {}, and located at:{}'.format(car, myList.index(car)+1))
else:
    print("sorry it can not be found in the list")


