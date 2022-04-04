# Football Points
# Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
# wins get 3 points
# draws get 1 point
# losses get 0 points


winPoints = 3
drawPoints = 1
lossPoint = 0

# Approach 1: Using Function
print("\n Approach 1 : Using Function")


def getScore(wins, draws, loss):
    total = (wins * winPoints) + (draws * drawPoints) + (loss * lossPoint)
    return total


team1 = getScore(5, 2, 1)
print("Score of Team 1 = ", team1)


# Approach 2 : Using Class and objects

print("\n Approach 2 : Using Class and objects")


class football:
    #initializing points for wins, losses, draws
    def __init__(self, wPt, dPt, lPt):
        self.wins = wPt
        self.draw = dPt
        self.loss = lPt

    def calcScore(self, w, d, l):
        w = w * self.wins
        d = d * self.draw
        l = l * self.loss
        total = w + d + l
        return total


t2 = football(winPoints, drawPoints, lossPoint)
t2Score = t2.calcScore(8, 3, 1)

print("Score of Team 2 = ", t2Score)
