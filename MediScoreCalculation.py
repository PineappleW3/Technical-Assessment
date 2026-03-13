from enum import IntEnum
import TimeTracker
#Uses enums to improve code readability
class oxygen(IntEnum):
     yes = 2
     no = 0

class conscious(IntEnum):
    yes = 0
    no = 1

class glucose(IntEnum):
    fasting = 0
    eating = 1

#Creates an object of the TimeTracker class
#This class is used to track increases in the patients calculated score in the past 24 hours
TrendTracker = TimeTracker()

#Function to calculate the Medi Score of a patient
#Used as a basic measure to detect ill patients
#Accounts for respiration rate, oxygen saturation, level of consciousness, temperature and whether the patient currently requires supplemental oxygen
#Also accounts for the capillary blood glucose, which can affect the score differently if the patient is fasting
def MediScoreCalculation(OnOxygen, Consciousness, RespirationRate, SPO2, Temperature, CBG, Fasting):
    #Sets initial score to zero, so it can be added to by each measured statistic
    score = 0

    #Uses a match case statement to calculate the score increase from whether the patiuent currently requires supplemental oxygen
    #0 represents no oxygen, and 2 represents oxygen
    #Uses an enum class to improve readability
    #All other values are out of range and invalid
    #Adds two points if patient is on oxygen
    match OnOxygen:
        case oxygen.no:
            pass
        case oxygen.yes:
            score +=2
            
    #Uses an if else statement to calculate the score increase from the patients consciousness status
    #0 represents consciousness, while any other non-zero integer represents CVPU
    #Uses an enum class to improve readability, however the no value cannot be used for the CVPU check as the value could be any non-zero integer
    #Instead, not yes is used, as this achieves the same result
    #Adds three points if the patient is CVPU
    if Consciousness == conscious.yes:
        pass
    elif Consciousness != conscious.yes:
        score +=3
    
    #Uses an if else statement to calculate the score increase from the patients respiration rate
    #three points are given if the value is less than or equal to 8, or greater than or equal to 25
    #two points are given for values between 21 and 24, one point for values between 9 and 11, and no points for values between 12 and 20
    if RespirationRate <= 8:
        score +=3
    elif RespirationRate >= 9 and RespirationRate <= 11:
        score +=1
    elif RespirationRate >= 12 and RespirationRate <= 20:
        pass
    elif RespirationRate >= 21 and RespirationRate <= 24:
        score +=2
    elif RespirationRate >= 25:
        score +=3

    #Uses two if else statements to calculate the score increase from the patients oxygen saturation
    #Needs two statements, since the score increases are dependent on if the patient is currently on oxygen
    if OnOxygen == oxygen.no:
        #If the patient is not on oxygen, they gain three points if the value is less than or equal to 83, two if it is between 84 and 85, one if it is betwene 86 and 87, and none for values greater than 88
        if SPO2 <= 83:
            score +=3
        elif SPO2 >= 84 and SPO2 <= 85:
            score +=2
        elif SPO2 >= 86 and SPO2 <= 87:
            score +=1
        elif SPO2 >= 88:
            pass

    else:
        #If the patient is on oxygen, they gain the same points as patients not on oxygen for values lower than 92, however now gain one point for values between 93 and 94,
        #two points for values between 95 and 96, and three points for values greater than 97
        if SPO2 <= 83:
            score +=3
        elif SPO2 >= 84 and SPO2 <= 85:
            score +=2
        elif SPO2 >= 86 and SPO2 <= 87:
            score +=1
        elif SPO2 >= 88 and SPO2 <= 92:
            pass
        elif SPO2 >= 93 and SPO2 <= 94:
            score +=1
        elif SPO2 >= 95 and SPO2 <= 96:
            score +=2
        elif SPO2 >= 97:
            score +=3

    #Uses an if statement to score increase from the patients temperature
    #Three points are given for values less than or equal to 35, two for values greater than or equal to 39.1, one for ranges 35.1–36 and 38.1–39, and none for 36.1–38 
    if Temperature <= 35:
        score +=3
    elif Temperature > 35 and Temperature <= 36:
        score +=1
    elif Temperature > 36 and Temperature <= 38:
        pass
    elif Temperature > 38 and Temperature <= 39:
        score +=1
    elif Temperature > 39:
        score +=2

    #Uses two if else statements to calculate the score increase from the patients capillary blood glucose
    #Needs two statements, since the score increases are dependent on if the patient is currently fasting or not
    #I was unsure if these new increases meant the score should still have a max of 14, or if the max should be increased to account for them
    #I chose to allow the max to increase along with the new source of points
    if Fasting == glucose.fasting:
        #If the patient is fasting, they gain three points if the value is less than or equal to 3.4, or greater than 6
        #They will gain 2 points for values in the ranges 3.5-3.9 and 5.5-5.9, and none for 4-5.4
        if CBG <= 3.4:
            score +=3
        elif CBG > 3.4 and CBG <= 3.9:
            score +=2
        elif CBG > 3.9 and CBG <= 5.4:
            pass
        elif CBG > 5.4 and CBG <= 5.9:
            score +=2
        elif CBG > 5.9:
            score +=3

    else:
        #If the patient is 2 hours after eating, they gain three points if the value is less than or equal to 4.5, or greater than 9
        #They will gain 2 points for values in the ranges 4.6-5.8 and 7.9-8.9, and none for 5.9-7.8
        #In the initial documentation one of the ranges is listed as 4.5-5.8, however this would mean that a value of 4.5 would qualify for both 2 and 3 points
        #For this reason, I have changed the interval to 4.6-5.8
        if CBG <= 4.5:
            score +=3
        elif CBG > 4.5 and CBG <= 5.8:
            score +=2
        elif CBG > 5.8 and CBG <= 7.8:
            pass
        elif CBG > 7.8 and CBG <= 8.9:
            score +=2
        elif CBG > 8.9:
            score +=3

    #Uses the Tracker object to find any rising trends in the score, and alerts the user if any are found
    Concerns = TrendTracker.AddScore(score)
    if Concerns == 1:
        print("The patients calculated score has risen by more than 2 over the past 24 hours. This could indicate additional risks to their health.")

    return score
