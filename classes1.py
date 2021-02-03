class footballPlayer:
    def __init__(self, first, last, height, weight, teamNumber, team):
        self.first=first
        self.last=last
        self.height=height
        self.weight=weight
        self.teamNumber=teamNumber
        self.team=team

    def printDetails(self):
        print('firstName:{}, LastName:{}, height:{}, weight:{}, teamNumber:{}, team:{}'.format(self.first, self.last, self.height, self.weight, self.teamNumber, self.team))

player1=footballPlayer('Idan', 'Ergaz', 1.83, 75, 10, 'Barcelona')
player2=footballPlayer('Naty', 'Shimon', 1.70, 56, 9, 'Rishonim')


player1.printDetails()
player2.printDetails()

player1.weight-=3
print("Player1 new weight:", player1.weight)
player2.team="Macabi"
print('Player2 new Team is:', player2.team)