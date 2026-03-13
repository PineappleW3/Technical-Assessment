from enum import IntEnum

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


#Function to validate the range and datatype of all inputted parameters
#These would likely be already validated by whatever previous process had them inputted, however for the sake of completeness they are also validated here
#This could be handled differently depending on the structure of the system
#For example, float datatypes could be cast to int datatypes, and vice versa
#For the sake of this implementation, I chose to allow the user to re-input the correct information, and then call the function again
def ValidateParameters(OnOxygen, Consciousness, RespirationRate, SPO2, Temperature, CBG, Fasting):
    #Validates the OnOxygen parameter
    #Should be equal to 0 or 2
    #Checking for these also ensures that the value given is an integer
    if OnOxygen != oxygen.yes and OnOxygen != oxygen.no:
        print("OnOxygen outside of expected range.")

        #Casts input to lower case to avoid issues with case
        #Also removes whitespace to avoid related issues
        NewOxygen = input("Does the patient currently require supplemental oxygen? (y/n) ").lower().strip()

        #Sets the relevant integer value based on input
        #If input is invalid, this code will be run again by repeat function calls
        match NewOxygen:
            case "y":
                OnOxygen = oxygen.yes
            case "n":
                OnOxygen = oxygen.no

        #Returns a repeat function call with newly inputted correct values
        return ValidateParameters(OnOxygen, Consciousness, RespirationRate, SPO2, Temperature, CBG, Fasting)
    
    #Validates the Consciousness parameter
    #Should be an integer of any value, since any non-zero value is treated as CVPU
    if type(Consciousness) != int:
        print("Consciousness outside of expected range.")

        #Casts input to lower case to avoid issues with case
        #Also removes whitespace to avoid related issues
        NewConsciousness = input("Is the patient conscious? (y/n) ").lower().strip()

        #Sets the relevant integer value based on input
        #If input is invalid, this code will be run again by repeat function calls
        match NewConsciousness:
                case "y":
                    Consciousness = int(conscious.yes)
                case "n":
                    Consciousness = int(conscious.no)

        #Returns a repeat function call with newly inputted correct values
        return ValidateParameters(OnOxygen, Consciousness, RespirationRate, SPO2, Temperature, CBG, Fasting)
    
    #Validates the RespirationRate parameter
    #Should be an integer of any value
    if type(RespirationRate) != int:
        print("RespirationRate outside of expected range.")

        #Casts input to int datatype as default datatype from input is string
        #Uses try except to avoid errors from inalid inputs
        #In case of invalid inputs, assigns an invalid value to the RespirationRate parameter to ensure this section of code is called again
        try:
            RespirationRate = int(input("What is the respiration rate of the patient? (should be an integer value) "))
        except:
            RespirationRate = "invalid"

        #Returns a repeat function call with newly inputted correct values
        #Function call will reach this code again if given input is invalid
        return ValidateParameters(OnOxygen, Consciousness, RespirationRate, SPO2, Temperature, CBG, Fasting)
    
    #Validates the SPO2 parameter
    #Should be an integer of any value
    if type(SPO2) != int:
        print("SPO2 outside of expected range.")

        #Casts input to int datatype as default datatype from input is string
        #Uses try except to avoid errors from inalid inputs
        #In case of invalid inputs, assigns an invalid value to the RespirationRate parameter to ensure this section of code is called again
        try:
            SPO2 = int(input("What is the oxygen saturation of the patient? (should be an integer value) "))
        except:
            SPO2 = "invalid"

        #Returns a repeat function call with newly inputted correct values
        #Function call will reach this code again if given input is invalid
        return ValidateParameters(OnOxygen, Consciousness, RespirationRate, SPO2, Temperature, CBG, Fasting)

    #Validates the Temperature parameter
    #Should be a float value to one decimal place
    if type(Temperature) != float and type(Temperature) != int:
        print("Temparature outside of expected range.")

        #Casts input to float datatype as default datatype from input is string
        #Uses try except to avoid errors from inalid inputs
        #In case of invalid inputs, assigns an invalid value to the Temperature parameter to ensure this section of code is called again
        try:
            Temperature = float(input("What is the temperature of the patient? (should be to one decimal place) "))
        except:
            Temperature = "invalid"

        #Returns a repeat function call with newly inputted correct values
        #Function call will reach this code again if given input is invalid
        return ValidateParameters(OnOxygen, Consciousness, RespirationRate, SPO2, Temperature, CBG, Fasting)
    
    #Validates the CBG parameter
    #Should be a float value
    if type(CBG) != float and type(CBG) != int:
        print("CBG outside of expected range.")

        #Casts input to float datatype as default datatype from input is string
        #Uses try except to avoid errors from inalid inputs
        #In case of invalid inputs, assigns an invalid value to the CBG parameter to ensure this section of code is called again
        try:
            CBG = float(input("What is the capillary blood glucose of the patient? "))
        except:
            CBG = "invalid"

        #Returns a repeat function call with newly inputted correct values
        #Function call will reach this code again if given input is invalid
        return ValidateParameters(OnOxygen, Consciousness, RespirationRate, SPO2, Temperature, CBG, Fasting)
    
    #Validates the Fasting parameter
    #Should be equal to 0 or 1
    #Checking for these also ensures that the value given is an integer
    if Fasting != glucose.fasting and Fasting != glucose.eating:
        print("Fasting outside of expected range.")

        #Casts input to lower case to avoid issues with case
        #Also removes whitespace to avoid related issues
        NewFasting = input("Is the patient currently fasting? (y/n) ").lower().strip()

        #Sets the relevant integer value based on input
        #If input is invalid, this code will be run again by repeat function calls
        match NewFasting:
            case "y":
                Fasting = glucose.fasting
            case "n":
                Fasting = glucose.eating

        #Returns a repeat function call with newly inputted correct values
        return ValidateParameters(OnOxygen, Consciousness, RespirationRate, SPO2, Temperature, CBG, Fasting)

    
    return [OnOxygen, Consciousness, RespirationRate, SPO2, Temperature, CBG, Fasting]