from enum import IntEnum
from datetime import datetime

#Uses an enum for increased readability
class concern(IntEnum):
     yes = 1
     no = 0


#Class used to store scores calculated and the time they were inputted
#Also calculates increasing trends in the score to alert the user for any risks
class TimeTracker():
    #Creates an empty list of scores
    def __init__(self):
        self.scores = []
    
    #Method to add a new score to the list, and then check it against all other scores from the past 24 hours
    def AddScore(self, score):
        #Appends the new score to the end of the list along with the time it was taken
        #Uses the datetime class to track time
        #Due to the nature of the list, it is always sorted, as scores can only be added in the order they were calculated
        self.scores.append([score, datetime.now()])

        #Calls a method to remove scores from the list from more than 24 hours before the newly added one was taken
        self.RemoveOld()

        #Returns the result of checking the list for an increasing trend
        return self.FindIncreases()

    #Method to remove scores from the list that were taken over 24 hours ago
    #These are not used in the calculation of finding trends, so are removed
    def RemoveOld(self):
        #Finds the time stored in the last entry in the list
        #Due to the list being ordered, this will always be the newest score
        TimeNow = self.scores[-1][1]

        #Finds the time 24 hours ago by creating a new datetime object whos day attribute is one less than the current day
        TimeYesterday = TimeNow.replace(day = (TimeNow.day - 1))

        #Finds the index of the first item in the list that happens after the time 24 hours ago
        #Removes all items before that index by using list slicing
        #This implementation ensures that if the first item in the list is from less than 24 hours ago, the list remains unchanged
        NewerIndex = 0

        #Iterates through every index, as range is not inclusive of the upper bound, and the length of a list is one more than the highest index
        for i in range (0,len(self.scores)):
            if self.scores[i][1] > TimeYesterday:
                NewerIndex = i
                #Breaks out when finding the first item less than 24 hours ago
                break

        #Uses list slicing to remove old elements
        self.scores = self.scores[NewerIndex:]
    

    #Method to find increases over time in scores taken in the past 24 hours
    def FindIncreases(self):
        #Finds the score stored in the last entry in the list
        #Due to the list being ordered, this will always be the newest score
        NewestScore = self.scores[-1][0]

        #Finds the score that is compared against to find increases
        #Since this is defined as an increase in over 2, I subtract 2 from the newest score and then find any values less than this
        ScoreToBeat = NewestScore - 2

        #Iterates through the entire list, and returns yes using an enum if any value less than the calculated score is found
        #Returns no otherwise
        for i in self.scores:
            if i[0] < ScoreToBeat:
                return concern.yes
        return concern.no